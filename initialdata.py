from requests.packages.urllib3.util.retry import Retry
import firebase_admin
from firebase_admin import credentials
#from firebase_admin import db
import pyrebase

config = {
    'apiKey': "AIzaSyCOo8XLTPqPUXifnsr_i5grdhtOrP7hiQk",
    'authDomain': "depression-classifier.firebaseapp.com",
    'databaseURL': "https://depression-classifier-default-rtdb.firebaseio.com",
    'projectId': "depression-classifier",
    'storageBucket': "depression-classifier.appspot.com",
    'messagingSenderId': "597961088303",
    'appId': "1:597961088303:web:0916129e5ee61e958a15da",
    'measurementId': "G-29W911PJMX",
    'databaseURL': 'https://depression-classifier-default-rtdb.firebaseio.com/'
  }

firebase =pyrebase.initialize_app(config)
db = firebase.database()
db.child('Prediction').push({
    "Patient":"patient_0",
    "Diagnosis":"Depressed",
    })

#dbref = db.reference('Psychiatrist')

#dbref.push({
 #   "Full_Name":"Lisa Davids",
  #  "Address":"A108 Adam Street, New York, NY 535022",
   # "Phone":"+12014222730",
    #"Email":"lisadavids161@gmail.com"
#})

#users_ref = ref.child('users')
#patients_ref = ref.child('patients')


