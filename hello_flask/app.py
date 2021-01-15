#This is the original hello_app. This file is separated into multiples files stored in hello_app folder for future development 

from flask import Flask, render_template
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    return render_template(
        "hello.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")
