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
    return render_template("index.html", page_title="Doggie Daycare", doggie=data)

@app.route('/about')
def about():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="Doggie About")

@app.route('/contact', methods=['POST', 'GET'])
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

@app.route('/grooming', methods=['POST', 'GET'])
def grooming():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("grooming.html", page_title="Doggie Grooming", doggie=data)
    

@app.route('/insert_booking', methods=['POST'])
def insert_booking():
    doggiebook = mongo.db.doggiebook
    doggiebook.insert_one(request.form.to_dict())
    return redirect(url_for('confirm'))


@app.route('/confirm')
def confirm():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("confirm.html", page_title="Doggie Confirmation", doggie=data)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        existing_user = mongo.db.doggielogin.find_one(
            {"email_address": request.form.get("email_address").lower()})

        if existing_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['email_address'] = request.form['email_address']
                return redirect(url_for('index'))

    return 'Invalid username/password combination'
    
    
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
            doggielogin.insert({'email_address' : request.form['email_address'],  'password' : hashpass, 'first_name' : request.form['first_name'], 'last_name' : request.form['last_name'], 'petname' : request.form['petname'], })
            session['email_address'] = request.form['email_address']
            return redirect(url_for('confirm'))
        return 'That username already exists!'

    return render_template("register.html", page_title="Doggie Register", doggie=data)

@app.route('/overnight')
def overnight():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("overnight.html", page_title="Doggie Sleepover", doggie=data)

@app.route('/prices')
def prices():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("prices.html", page_title="Doggie Prices", doggie=data)

@app.route('/viewbooking')
def viewbooking():
    return render_template('viewbooking.html',
                           doggiebook=mongo.db.doggiebook.find())

@app.route('/edit_booking/<task_id>', methods=['POST', 'GET'])
def edit_booking(task_id):
    the_task =  mongo.db.doggiebook.find_one({"_id": ObjectId(task_id)})
    edit_login =  mongo.db.doggielogin.find()
    edit_pets = mongo.db.doggiepets.find()
    return render_template('editbooking.html', task=the_task, login=edit_login, pets=edit_pets)


@app.route('/update_booking/<task_id>', methods=["POST"])
def update_booking(task_id):
    tasks = mongo.db.doggiebook
    tasks.update( {'_id': ObjectId(task_id)},
    {
        'email_address':request.form.get('email_address'),
        'petname':request.form.get('petname'),
        'service': request.form.get('service'),
        'date': request.form.get('date')
    })
    return redirect(url_for('viewbooking'))

@app.route('/delete_booking/<task_id>')
def delete_booking(task_id):
    mongo.db.doggiebook.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('viewbooking'))

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)