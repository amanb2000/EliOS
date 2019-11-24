from functools import wraps
import firebase_admin
import atexit
import time
from firebase_admin import credentials, firestore
from datetime import date, datetime, timedelta
from flask import Flask, g, session, redirect, url_for, request, current_app, make_response
from functools import update_wrapper
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
# Add Secret Key
app.secret_key = app.config['SECRET_KEY']
# Add DB
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

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
      print("meow")
   return

# Add Job scheduler
cron = BackgroundScheduler()

# Add auto-triggered tasks
cron.add_job(func=train_model, trigger='interval', hours=6)
cron.start()

# Shutdown scheduler on close
# atexit.register(lambda: cron.shutdown(wait=False))

from eli import fetcher