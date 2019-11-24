import firebase_admin
from cts import app, crossdomain, get_conn
from firebase_admin import firestore
from json import dumps
from uuid import uuid4
from flask import request
import requests

@app.route("/processSignal", methods=["POST", 'GET'])
@crossdomain(origin='*')
def get_patients():

   if request.form.get('postkey') != app.config['POST_KEY']: # Secures the data with a key
      return ""

   

   doc_ref = get_conn().collection('patients')

   patients = []

   for row in doc_ref.get():
      patient = row.to_dict()
      patient.pop('name', None)
      patient['id'] = str(uuid4()).replace('-','')
      patient['days'] = []
      for row in doc_ref.document(row.id).collection('days').get():
         patient['days'] += [row.to_dict()]
      patients += [patient]

   return dumps(patients)

@app.route("/test")
def meow():
   return "Welcome to the application test page"