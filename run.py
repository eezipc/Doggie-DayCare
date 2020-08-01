import os
import json
from flask import Flask, render_template

app = Flask(__name__)


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

@app.route('/login')
def login():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("login.html", page_title="Doggie Login", doggie=data)

@app.route('/overnight')
def overnight():
    data = []
    with open("data/doggie.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("overnight.html", page_title="Doggie Sleepover", doggie=data)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)