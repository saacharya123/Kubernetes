from flask import Flask,request
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

@app.route ('/signup',methods=['POST'])
def signup():

    form_data = request.get_json() 
    name = form_data.get('name')
    email = form_data.get('email')
    password = form_data.get('password')

    with open('users.txt', 'a') as file:
        file.write(f"Name: {name}, Email: {email}, Password: {password}\n")

        
    collection.insert_one(form_data)
    print(form_data)

    return f"signnedup suuccessfully...!!"

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
    app.run(host='0.0.0.0',port=9000,debug=True)