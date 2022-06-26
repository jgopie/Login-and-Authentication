from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import random
from datetime import datetime
from send_code import send_code

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/user_info"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)
    code = db.Column(db.String(6), unique=False, nullable=False)
    creation_time = db.Column(db.String(20), unique=False, nullable=False)
    verified = db.Column(db.Boolean(0), unique=False, nullable=False)
    phone_number = db.Column(db.String(20), unique=False, nullable=True)
    address = db.Column(db.String(50), unique=False, nullable=True)
    user_name = db.Column(db.String(10), unique=False, nullable=True)
    registration_complete = db.Column(db.Boolean(0), unique=False, nullable=True)


def create_user(email, password, verified):
    code = "".join([str(random.randint(0, 9)) for _ in range(0, 6)])
    time_of_creation = (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
    new_user = User(email=email, password=password, code=code, creation_time=time_of_creation, verified=verified)
    db.session.add(new_user)
    db.session.commit()
    send_code(code, email)


def verify_user(user):
    user.verified = True
    db.session.commit()


def complete_user_registration(user, user_name, address, phone_number, registration_complete):
    user.user_name = user_name
    user.address = address
    user.phone_number = phone_number
    user.registration_complete = registration_complete
    db.session.commit()
