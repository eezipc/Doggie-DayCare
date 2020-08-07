import os
import json
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'doggiedatabase'
app.config['MONGO_URI'] = 'mongodb+srv://doggieuser:doggiepassword@doggiecluster.wtitg.mongodb.net/doggiedatabase?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def index():
  
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", page_title="Home", doggie=data)



@app.route('/about')
def about():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="Doggie About")


@app.route('/test')
def test():
    return render_template("test.html", doggiebook=mongo.db.doggiebook.find())
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("test.html", page_title="Doggie About")



@app.route('/contact')
def contact():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("contact.html", page_title="Doggie Contact")

@app.route('/daycare')
def daycare():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("daycare.html", page_title="Doggie Daycare", doggie=data)

@app.route('/grooming')
def grooming():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("grooming.html", page_title="Doggie Grooming", doggie=data)

@app.route('/login', methods=['POST', 'GET'])
def login():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("login.html", page_title="Doggie Login", doggie=data)



@app.route('/loginpage', methods=['POST', 'GET'])
def loginpage():
    if 'email_address' in session:
        return 'You are logged in as ' + session['email_address']

    return render_template('loginpage.html')
    doggielogin = mongo.db.doggielogin
    login_user = doggielogin.find_one({'email_address': request.form['email_address']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['email_address'] = request.form['email_address']
            return redirect(url_for('loginpage'))

    return 'Invalid username or password'


@app.route('/register', methods=['POST', 'GET'])
def register():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)

    if request.method == 'POST':
        doggielogin = mongo.db.doggielogin
        existing_user = doggielogin.find_one({'email_address' : request.form['email_address']})
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            doggielogin.insert({'email_address' : request.form['email_address'],  'password' : hashpass, 'first_name' : request.form['first_name'], 'last_name' : request.form['last_name'], 'address' : request.form['address'], })
            session['email_address'] = request.form['email_address']
            return redirect(url_for('login'))
        
        return 'That username already exists!'

    return render_template("register.html", page_title="Doggie Register", doggie=data)

@app.route('/overnight')
def overnight():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("overnight.html", page_title="Doggie Sleepover", doggie=data)



if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)