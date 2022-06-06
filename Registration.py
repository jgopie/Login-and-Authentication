from __main__ import app
from flask import render_template, request, redirect, url_for
from users import User, create_user
from werkzeug.security import generate_password_hash


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_email = request.form["email"]
        user_password = request.form["password"]
        salted_password = generate_password_hash(password=user_password, method="pbkdf2:sha256", salt_length=8)
        new_user = User(email=user_email, password=salted_password)
        create_user(new_user)
        return redirect(url_for("login"))
    else:
        return render_template("index.html")
