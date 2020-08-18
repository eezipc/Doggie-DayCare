

import os
import json
from flask import Flask, render_template, redirect, request, url_for, session, flash, Markup
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

											#Connect Database
app.config['MONGO_DBNAME'] = 'doggiedatabase'
app.config['MONGO_URI'] = 'mongodb+srv://doggieuser:doggiepassword@doggiecluster.wtitg.mongodb.net/doggiedatabase?retryWrites=true&w=majority'


mongo = PyMongo(app)

#Index Page
@app.route('/')
def index():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", page_title="Doggie Daycare", doggie=data)

#About Page
@app.route('/about')
def about():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="Doggie About")

#Contact Page
@app.route('/contact', methods=['POST', 'GET'])
def contact():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("contact.html", page_title="Doggie Contact")

#Daycare Page
@app.route('/daycare')
def daycare():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("daycare.html", page_title="Doggie Daycare", doggie=data) 

#Grooming Page
@app.route('/grooming', methods=['POST', 'GET'])
def grooming():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("grooming.html", page_title="Doggie Grooming", doggie=data)
    
#Insert Booking Page
@app.route('/insert_booking', methods=['POST'])
def insert_booking():
    doggiebook = mongo.db.doggiebook
    doggiebook.insert_one(request.form.to_dict())
    return redirect(url_for('confirm'))

#Confirmation Page
@app.route('/confirm')
def confirm():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("confirm.html", page_title="Doggie Confirmation", doggie=data)


#Register Page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.doggielogin.find_one(
            {"email_address": request.form.get("email_address").lower()})
        if existing_user:
            flash("This Email Is Already Registered")
            return redirect(url_for("register"))
        register = {
            "email_address": request.form.get("email_address").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "petname": request.form.get("petname").lower()
        }
        mongo.db.doggielogin.insert_one(register)
        session["user"] = request.form.get("email_address").lower()
        flash("Congratulations, Your Account Has Been Registered")
        return redirect(url_for("profile", email_address=session["user"]))
    return render_template("register.html", page_title="Doggie Register")

#Login Page
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        existing_user = mongo.db.doggielogin.find_one(
            {"email_address": request.form.get("email_address").lower()})
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("email_address").lower()
                flash("Who's a Good Doggie?, {} is a Good Doggie".format(
                        request.form.get("email_address")))
                return redirect(url_for(
                        "profile", email_address=session["user"]))
            else:
                
                flash("Password is incorrect. Please Try again")
                return redirect(url_for("login"))
        else:
           
            flash("Sorry, we don't recognise that Email Address")
            return redirect(url_for("login"))
    return render_template("login.html", page_title="Doggie Login")

#Profile Page
@app.route("/profile/<email_address>", methods=['GET', 'POST'])
def profile(email_address):
    email_address = mongo.db.doggielogin.find_one(
       {"email_address": session["user"]})["email_address"]
    if session["user"]:
        return render_template("profile.html", email_address=email_address, page_title="Doggie Profile")
    return redirect(url_for("profile"))

#Logout Page
@app.route("/logout")
def logout():
    flash("You have been logged out..... Walkies?")
    session.pop("user")
    return redirect(url_for("index"))

#View Profile Page
@app.route("/viewprofile/<email_address>", methods=['GET', 'POST'])
def viewprofile(email_address):
    mongo.db.doggielogin.find_one({"email_address": session["user"]})
    return render_template('viewprofile.html',
                           doggielogin=mongo.db.doggielogin.find({"email_address": session["user"]}), page_title="View Profile")


#View Profile Booking Page
@app.route("/viewprofilebooking/<email_address>", methods=['GET', 'POST'])
def viewprofilebooking(email_address):
    mongo.db.doggiebook.find_one({"email_address": session["user"]})
    return render_template('viewprofilebooking.html',
                           doggiebook=mongo.db.doggiebook.find({"email_address": session["user"]}), page_title="View Profile Bookings")


#Edit Profile Page
@app.route('/editprofile/<email_address>', methods=['POST', 'GET'])
def editprofile(email_address):
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    the_task2 =  mongo.db.doggielogin.find_one({"email_address": session["user"]})
    return render_template('editprofile.html', task2=the_task2,  page_title="Doggie Edit Booking", doggie=data)


#Update profile Page
@app.route('/updateprofile/<email_address>', methods=['POST', 'GET'])
def updateprofile(email_address):
    tasksupdate = mongo.db.doggielogin
    tasksupdate.update({"email_address": session["user"]},
    {
        'email_address':request.form.get('email_address'),
        'password':request.form.get('password'),
        'petname':request.form.get('petname'),
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name')
    })
    return redirect(url_for('index'))

#Delete Profile Page
@app.route("/delete_profile/<email_address>", methods=["GET", "POST"])
def delete_profile(email_address):
    mongo.db.doggielogin.remove({"email_address": session["user"]})
    session.clear()
    flash("Goodbye")
    return redirect(url_for("index"))

#Overnight Page
@app.route('/overnight')
def overnight():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("overnight.html", page_title="Doggie Sleepover", doggie=data)

#Prices Page
@app.route('/prices')
def prices():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("prices.html", page_title="Doggie Prices", doggie=data)

#View Booking Page
@app.route('/viewbooking')
def viewbooking():
    return render_template('viewbooking.html',
                           doggiebook=mongo.db.doggiebook.find(), page_title="Doggie Bookings")

#Edit Booking Page
@app.route('/edit_booking/<task_id>', methods=['POST', 'GET'])
def edit_booking(task_id):
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    the_task =  mongo.db.doggiebook.find_one({"_id": ObjectId(task_id)})
    edit_login =  mongo.db.doggielogin.find()
    edit_pets = mongo.db.doggiepets.find()
    return render_template('editbooking.html', task=the_task, login=edit_login, pets=edit_pets, page_title="Doggie Edit Booking", doggie=data)


#Update Booking Page
@app.route('/update_booking/<task_id>', methods=['POST', 'GET'])
def update_booking(task_id):
    tasks = mongo.db.doggiebook
    tasks.update( {'_id': ObjectId(task_id)},
    {
        'email_address':request.form.get('email_address'),
        'petname':request.form.get('petname'),
        'service': request.form.get('service'),
        'date': request.form.get('date')
    })
    return redirect(url_for('index'))

#Delete Booking Page
@app.route('/delete_booking/<task_id>')
def delete_booking(task_id):
    mongo.db.doggiebook.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('index'))

#End of Run.py
if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)