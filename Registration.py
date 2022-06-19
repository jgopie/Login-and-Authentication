from __main__ import app
from flask import render_template, request, redirect, url_for
from users import User, create_user, complete_user_registration
from werkzeug.security import generate_password_hash
from flask_login import login_required


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_email = request.form["email"]
        user_password = request.form["password"]
        salted_password = generate_password_hash(password=user_password, method="pbkdf2:sha256", salt_length=8)
        create_user(email=user_email, password=salted_password, verified=False)
        return redirect(url_for("verify", user_email=user_email))
    else:
        return render_template("index.html")


@app.route("/register/<user_email>", methods=["GET", "POST"])
@login_required
def register(user_email):
    if request.method == "POST":
        user_info = User.query.filter_by(email=user_email).first()
        user_name = request.form["username"]
        phone_number = request.form["phone_number"]
        address = request.form["address"]
        registration_complete = True
        complete_user_registration(user=user_info, user_name=user_name, address=address, phone_number=phone_number, registration_complete=registration_complete)
        return redirect(url_for("view_profile", user_email=user_email))
    else:
        return render_template("complete_registration.html", user_email=str(user_email))

