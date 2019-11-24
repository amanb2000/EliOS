from elios import app, crossdomain, get_conn, request
import requests
import elios.analyzer as analis
import pandas as pd
from io import StringIO

@app.route("/processSignal", methods=["POST", 'GET'])
@crossdomain(origin='*')
def get_patients():

   if request.form.get('postkey') != app.config['POST_KEY']: # Secures the data with a key
      return ""

   day = request.form.get('day')
   uid = request.form.get('user')

   doc_ref = get_conn().collection('users').document(uid).collection('days').document(day)
   data = doc_ref.get().to_dict()

   eeg = data['EEG_URL']

   r = requests.get(eeg, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
   pd_in = pd.read_csv(StringIO(str(r.content, 'utf-8')))

   x = analis.aggregate_all_bands(pd_in)

   print(x)
   doc_ref.update(x)
   return ""
   

@app.route("/test")
def meow():
   requests.post("http://localhost:5000/processSignal", data={'postkey': app.config['POST_KEY'], 'user': 'ohUkwiFwOAdS9g0XqIESDDa3qbs1', 'day': 1574571600})
   return "Welcome to the application test page"