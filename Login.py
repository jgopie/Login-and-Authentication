from __main__ import app, login_manager
from flask import render_template, request, redirect
from users import User



@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_email = request.form["email"]
        user_password = request.form["password"]
    return render_template("login.html")
