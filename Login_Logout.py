from __main__ import app, login_manager
from flask import render_template, request, redirect, flash, url_for, session
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
        session["user_email"] = user_email
        user_password = request.form["password"]
        user_info = User.query.filter_by(email=user_email).first()
        check_pass = check_password_hash(user_info.password, user_password)
        if check_pass and user_info.verified == True:
            login_user(user_info)
            session.permanent = True
            return redirect(url_for("register", user_email=user_email))
        else:
            flash("Invalid Credentials")
            return redirect(url_for("login"))
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user_email", None)
    return redirect(url_for("login"))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("login"))
