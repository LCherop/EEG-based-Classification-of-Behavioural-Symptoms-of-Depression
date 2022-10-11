from flask import Flask,session, render_template, request, redirect
import pyrebase
#from flask_login import LoginManager
#login_manager  LoginManager

app = Flask(__name__)

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

#Add a secret key that encrypts the cookies session code
#app.secret_key - 'secret'

#Random landing page
@app.route("/")
def home():
    return render_template('login.html')

#Login route
@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    pass

#Register route
@app.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')


    
if __name__ == "__main__":
    app.run(debug=True)
