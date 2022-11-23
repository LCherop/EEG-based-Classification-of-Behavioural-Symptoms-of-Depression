import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("/home/laura/Documents/school/Sem 2/IS 2/firebase_tingzz/to_db.json")
firebase_admin.initialize_app(cred,{"https://depression-classifier-default-rtdb.firebaseio.com/"})

#ref = db.reference('https://console.firebase.google.com/u/0/project/depression-classifier/database/depression-classifier-default-rtdb/data/~2F')

#users_ref = ref.child('users')
#patients_ref = ref.child('patients')


