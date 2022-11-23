from flask import Flask,session, render_template, request, redirect,make_response,flash
import pyrebase
import firebase_admin
import os
from os.path import join,dirname,realpath
import joblib
from firebase_admin import credentials
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import numpy as np



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
app.secret_key = 'secret'
app.config['UPLOAD_FOLDER'] = 'static/files'
ALLOWED_EXTENSIONS = {'csv'}
f = ''


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


#Random landing page
@app.route("/")
def home():
    return render_template('login.html')


@app.route("/uploader",methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST':
        global f
        f = request.files['file']
        
        if f.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            #f.save(secure_filename(f.filename))
            fn_path = os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
            f.save(fn_path)
            return render_template('landing_page.html')

@app.route("/predict",methods = ['GET','POST'])
def predict():
    X = np.loadtxt(f.filename,delimiter=',')
    
    model = joblib.load("knn_model.pkl")
    t =''
    prediction = model.predict([X])
    if prediction == [1]:
        t = 'The patient has depression'
    else:
        t = 'The patient does not have depression'
    return render_template("landing_page.html",output = t)
            
     
#Login route
@app.route('/login', methods=['GET','POST'])
def login():
    if('user' in session):
        return render_template('landing_page.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email,password)
            session['user'] = email
        except:
            return 'Failed to login'
    return render_template('landing_page.html')


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

@app.route('/reset',methods=['GET','POST'] )
def reset():
    return render_template('reset.html')

@app.route('/send_email',methods=['GET','POST'] )
def send_email():
    if request.method == 'POST':
        email = request.form.get('email')
        try:
            user = auth.send_password_reset_email(email)
        except:
            return make_response('Email is not registered')
    return render_template('wait.html')



if __name__ == "__main__":
    
    app.run(debug=True)
