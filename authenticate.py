import pyrebase

config = {
    #Add config data to your database
  }

firebase =pyrebase.initialize_app(config)
auth = firebase.auth()

email = 'test@gmail.com'
password = '123456'

user = auth.create_user_with_email_and_password(email,password)
#print(user)


auth.send_email_verification(user['idToken'])

auth.send_password_reset_email(email)
