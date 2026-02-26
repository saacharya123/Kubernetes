from flask import Flask,render_template,request
from datetime import datetime
import requests
import os

BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:9000')



app=Flask(__name__)
@app.route('/')
def home():
    now = datetime.now()
    day_of_week = now.strftime('%A')
    current_time = now.strftime('%I:%M:%S %p')

    return render_template('index.html', day=day_of_week, time=current_time)

@app.route ('/signup',methods=['POST'])
def signup():

    # FRONTEND reads FORM data
    form_data = dict(request.form)

    # FRONTEND sends JSON to backend
    requests.post(BACKEND_URL + '/signup', json=form_data)
   
    return f"HOLAAA... SIGNEDUP!!"


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)