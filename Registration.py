from __main__ import app
from flask import Flask, render_template, redirect, request
from users import User, create_user


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_email = request.form["email"]
        user_password = request.form["password"]
        new_user = User(email=user_email, password=user_password)
        create_user(new_user)
    return render_template("index.html")
