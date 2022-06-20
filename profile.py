from flask_login import login_required, login_manager
from flask import render_template, redirect, url_for
from __main__ import app
from users import User


@app.route("/profile/<user_name>")
@login_required
def view_profile(user_name):
    user_info = User.query.filter_by(user_name=user_name).first()
    return render_template("profile.html", user_name=user_info.user_name, phone_number=user_info.phone_number, address=user_info.address)
