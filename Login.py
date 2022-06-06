from __main__ import app, login_manager
from flask import render_template, request, redirect, flash
from users import User
from werkzeug.security import check_password_hash
from flask_login import login_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_email = request.form["email"]
        user_password = request.form["password"]
        user_info = User.query.filter_by(email=user_email).first()
        check_pass = check_password_hash(user_info.password, user_password)
        if check_pass:
            login_user(user_info)
            return render_template("secret.html")
        else:
            flash("Invalid Credentials")
    else:
        return render_template("login.html")
