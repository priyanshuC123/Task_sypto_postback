#So firstly we have to host this app and use that as the base url for the webhook/postback url and use /fyers as the route 
#and the api will make source to trigger the webhook url when the order is placed in fyers.

#this is a simple application that sends a email using mailtrap services to the desired 
#response email that we can get from the fyers

#to check you can use http://127.0.0.1:5000/fyers as the webhook link as i have not hoste the applicationn

from flask import Flask, request
import json
from flask_mail import Mail,Message

app = Flask(__name__)

app.config['MAIL_SERVER']='live.smtp.mailtrap.io'
app.config['MAIL_PORT']=587
app.config['MAIL_USERNAME']='api'
app.config['MAIL_PASSWORD']='4d8647025e4a807db843c13a4e778a3d'
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False

mail = Mail(app)

@app.route('/fyers',methods=['GET', 'POST'])
def fyers():
    if request.content_type == 'application/json' :
        json_data = request.json
        if json.dumps(json_data) is not None : 

            message = Message(
            subject ="Hello",
            recipients=['priyanschoudhary100@gmail.com'],
            sender='mailtrap@demomailtrap.com'
            )
            message.body = 'Placed New Buy Order'
            mail.send(message)
            return 'message sent!'
   
    return "Unable to read Message"

@app.route('/',methods=['GET', 'POST'])
def home():
    return 'All is well'

if __name__ == "__main__":
    app.run(debug=True)