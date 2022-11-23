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
    'databaseURL': ''
  }

firebase =pyrebase.initialize_app(config)
auth = firebase.auth()

email = 'test@gmail.com'
password = '123456'

user = auth.create_user_with_email_and_password(email,password)
#print(user)


auth.send_email_verification(user['idToken'])

auth.send_password_reset_email(email)