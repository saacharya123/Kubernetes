from flask import Flask,render_template,request
from datetime import datetime
import os
import csv
from  dotenv import load_dotenv
import pymongo

load_dotenv()
MONGO_URL=os.getenv('MONGO_URI')

client=pymongo.MongoClient(MONGO_URL)
db=client.test
collection=db['flask-tutorial']


app=Flask(__name__)
@app.route('/')
def home():
    now = datetime.now()
    day_of_week = now.strftime('%A')
    current_time = now.strftime('%I:%M:%S %p')

    return render_template('index.html', day=day_of_week, time=current_time)

@app.route ('/signup',methods=['POST'])
def signup():
    name=request.form.get('name')
    first_name=name.split()[0]
    email=request.form.get('email')

    
    form_data=dict(request.form)
    with open('users.txt', 'a') as file:
        file.write(
            f"Name: {request.form.get('name')}, "
            f"Email: {request.form.get('email')}, "
            f"Password: {request.form.get('password')}\n"
        )


    collection.insert_one(form_data)
    print(form_data)

    return f"{first_name} signnedup suuccessfully...!!"

@app.route('/view')
def view():
    data=collection.find()
    data=list(data)
    for item in data:
        print(item)
        del item['_id']
    
    data={'data': data}

    return data

if __name__=='__main__':
    app.run(debug=True)