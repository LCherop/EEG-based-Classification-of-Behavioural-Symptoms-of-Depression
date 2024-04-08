from requests.packages.urllib3.util.retry import Retry
import firebase_admin
from firebase_admin import credentials
#from firebase_admin import db
import pyrebase


config = {
    #Add config data to your database
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


