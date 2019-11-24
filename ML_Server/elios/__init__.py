from functools import wraps
import atexit
import time
from firebase_admin import credentials, firestore, initialize_app
from datetime import date, datetime, timedelta
from flask import Flask, g, session, redirect, url_for, request, current_app, make_response
from functools import update_wrapper
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from sklearn.neural_network import MLPRegressor
import numpy as np

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
# Add Secret Key
app.secret_key = app.config['SECRET_KEY']
# Add DB
cred = credentials.Certificate('serviceAccountKey.json')
initialize_app(cred, {'name': 'initial'})

# Build cross-domain allowing wrapper

def crossdomain(origin=None, methods=None, headers=None, max_age=21600,
                attach_to_all=True, automatic_options=True):
   if methods is not None:
      methods = ', '.join(sorted(x.upper() for x in methods))
   if headers is not None:
      headers = ', '.join(x.upper() for x in headers)
   if origin is not None:
      origin = ', '.join(origin)
   if isinstance(max_age, timedelta):
      max_age = max_age.total_seconds()

   def get_methods():
      if methods is not None:
         return methods

      options_resp = current_app.make_default_options_response()
      return options_resp.headers['allow']

   def decorator(f):
      def wrapped_function(*args, **kwargs):
         if automatic_options and request.method == 'OPTIONS':
               resp = current_app.make_default_options_response()
         else:
               resp = make_response(f(*args, **kwargs))
         if not attach_to_all and request.method != 'OPTIONS':
               return resp

         h = resp.headers
         h['Access-Control-Allow-Origin'] = origin
         h['Access-Control-Allow-Methods'] = get_methods()
         h['Access-Control-Max-Age'] = str(max_age)
         h['Access-Control-Allow-Credentials'] = 'true'
         h['Access-Control-Allow-Headers'] = \
               "Origin, X-Requested-With, Content-Type, Accept, Authorization"
         if headers is not None:
               h['Access-Control-Allow-Headers'] = headers
         return resp

      f.provide_automatic_options = False
      return update_wrapper(wrapped_function, f)
   return decorator


# Make DB fetcher
def get_conn():
   if 'conn' in g and g.conn is not None:
      return g.conn
   else:
      g.conn = firestore.client()
      return g.conn

# Add json serializiation extender

def json_serial(obj):
   """JSON serializer for non JSON serializable objects"""

   if isinstance(obj, (datetime, date)):
      return obj.isoformat()
   # elif isinstance(obj, (Decimal.Decimal)):
   #    return float(obj)
   raise TypeError ("Type {} is not serializable".format(type(obj)))

# CREATE SCHEDULED ACTIONS
def train_model():
   with app.app_context():
      doc_ref = get_conn().collection('users')

      for row in doc_ref.get():
         user = row.to_dict()
         frames = []
         for dt in doc_ref.document(row.id).collection('days').where("epoch", ">",  int(time.time()) - 604800).get():
            day = dt.to_dict()
            new_day = {}
            new_day['Diagnosis'] = user['diagnosis'] if 'diagnosis' in user else None
            new_day['Dob'] = user['dob'] if 'dob' in user else None
            new_day['Gender'] = user['gender'] if 'gender' in user else None

            new_day['Sleep'] = day['sleep'] if 'sleep' in day else None
            new_day['Sleep Chunks'] = day['sleepChunks'] if 'sleepChunks' in day else None
            new_day['Mood'] = day['mood'] if 'mood' in day else None
            new_day['Calories'] = day['calories'] if 'calories' in day else None

            new_day['Exercise Duration'] = day['exerciseDuration'] if 'exerciseDuration' in day else None
            new_day['Exercise Intensity'] = day['exerciseIntensity'] if 'excersiseIntencity' in day else None

            new_day['Alpha'] = day['alpha'] if 'alpha' in day else None
            new_day['Beta'] = day['beta'] if 'beta' in day else None
            new_day['Theta'] = day['theta'] if 'theta' in day else None
            new_day['Gamma'] = day['gamma'] if 'gamma' in day else None
            frames = [new_day] + frames

         if len(frames) < 1: continue
         # Getting the X and y variable set up:
         X = np.column_stack( ( np.asarray(frames[0]['Sleep']), np.asarray(frames[0]['Sleep Chunks']), np.asarray(frames[0]['Calories']), np.asarray(frames[0]['Mood']), np.asarray(frames[0]['Exercise Duration']), np.asarray(frames[0]['Exercise Intensity']),  np.asarray(frames[0]['Alpha']), np.asarray(frames[0]['Beta']), np.asarray(frames[0]['Theta']), np.asarray(frames[0]['Gamma']) ) )
         y = np.column_stack( (np.asarray(frames[1]['Mood'])) )

         for i in range(1, len(frames)-1):
            X_cur = np.column_stack( ( np.asarray(frames[i]['Sleep']), np.asarray(frames[i]['Sleep Chunks']), np.asarray(frames[i]['Calories']), np.asarray(frames[i]['Mood']), np.asarray(frames[i]['Exercise Duration']), np.asarray(frames[i]['Exercise Intensity']),  np.asarray(frames[i]['Alpha']), np.asarray(frames[i]['Beta']), np.asarray(frames[i]['Theta']), np.asarray(frames[i]['Gamma']) ) )
            y_cur = np.column_stack( (np.asarray(frames[i+1]['Mood'])) )
            
            X = np.append(X, X_cur, axis=0)
            y = np.append(y, y_cur)

         # Training Model: 
         clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(7, 6), random_state=1)
         clf.fit(X, y)

         def predictTomorrow(row): #Row is of form `frames[0].loc[1]`
            x_obj = np.asarray([ row['Sleep'],row['Sleep Chunks'],row['Calories'],row['Mood'],row['Exercise Duration'],row['Exercise Intensity'], row['Alpha'],row['Beta'],row['Theta'],row['Gamma'] ])
            y_pred = clf.predict(np.reshape(x_obj, (1, -1)))
            return y_pred[0]

         tmo = predictTomorrow(frames[6].loc[1])
         print(tmo)
         doc_ref.document(row.id).collection('days').document(dt.id).update({'moodpred': tmo})
   return



# Add Job scheduler
cron = BackgroundScheduler()

# Add auto-triggered tasks
cron.add_job(func=train_model, trigger='interval', seconds=30)
cron.start()

# Shutdown scheduler on close
# atexit.register(lambda: cron.shutdown(wait=False))

from elios import process, analyzer
