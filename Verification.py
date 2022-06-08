from __main__ import app
from flask import render_template, request, flash, redirect, url_for
from users import User, verify_user


@app.route("/verify/<string:user_email>", methods=["GET", "POST"])
def verify(user_email):
    if request.method == "POST":
        email = str(user_email)
        code = request.form["code"]
        user_info = User.query.filter_by(email=email).first()
        user_code = user_info.code
        if user_code == code:
            verify_user(user_info)
            return redirect(url_for("login"))
        else:
            flash("Incorrect code")
    else:
        return render_template("verify.html", user_email=str(user_email))
