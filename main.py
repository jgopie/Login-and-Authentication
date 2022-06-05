from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import smtplib
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tmp.test.db"
db = SQLAlchemy(app)

send_email = "jordangopietest@yahoo.com"
email_pass = "Dwk-vH-Er3_2ZAn"
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)


db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method =="POST":
        user_email = request.form.get("email")
        user_password = request.form.get("password")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
