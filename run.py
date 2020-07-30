import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/daycare')
def daycare():
    return render_template("daycare.html")

@app.route('/grooming')
def grooming():
    return render_template("grooming.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/overnight')
def overnight():
    return render_template("overnight.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)