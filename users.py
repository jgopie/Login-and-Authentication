from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import random
from datetime import datetime

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_info.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)




class User(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)
    code = db.Column(db.String(6), unique=False, nullable=False)
    creation_time = db.Column(db.String(20), unique=False, nullable=False)

# db.create_all()
def create_user(email, password):
    code = "".join([str(random.randint(0, 9)) for _ in range(0, 6)])
    time_of_creation = (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
    new_user = User(email=email, password=password, code=code, creation_time=time_of_creation)
    db.session.add(new_user)
    db.session.commit()
