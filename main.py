from flask import Flask,render_template,request,url_for,redirect
import os
from dotenv import load_dotenv
from flask_mail import Mail,Message

app = Flask(__name__)
load_dotenv()
mail = Mail(app)


_USER=os.getenv("_USER")
PASSWORD=os.getenv("PASSWORD")
RECI=os.getenv("RECI")
SKEY=os.getenv("SKEY")




app.config["SECRET_KEY"]=SKEY#encrypt cookies n session data
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = _USER # developer mail here
app.config['MAIL_PASSWORD'] = PASSWORD     #mail password here, I suggest you use enviroment variables, 
                                                            #google how to use it with flask, and also don't 
                                                            #forget to add it to production too
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

@app.route('/sendmail', methods=['GET', 'POST'])
def sendmail():  
        message= request.form['message']    
        msg = Message(
            'Portfilio Responses', 
            sender = _USER, 
            recipients = [RECI]
            )  # Please input the emails in the appropriate fields
        msg.body = "this is the feedback : {}".format(message)
        mail.send(msg)

        return redirect(url_for('thankyou'))

    
    



@app.route('/', methods=['GET', 'POST'])
def home():        
    return render_template("index.html")


@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    return render_template("thankyou.html")

if __name__=="__main__":   
    app.run(debug=True)