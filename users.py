from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)


def create_user(user_to_add):
    db.session.add(user_to_add)
    db.session.commit()
