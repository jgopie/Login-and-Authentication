from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import smtplib
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)


db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_email = request.form["email"]
        user_password = request.form["password"]
        new_user = User(email=user_email, password=user_password)
        db.session.add(new_user)
        db.session.commit()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
