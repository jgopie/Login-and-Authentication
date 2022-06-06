from flask import Flask
from flask_login import LoginManager
import smtplib
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "454cc9133a0c32b0187199c9dff7328a71c5a2199494af48eeba0ad4d948781d"
login_manager = LoginManager()
login_manager.init_app(app)

import Registration
import Login
import Verification

if __name__ == "__main__":
    app.run(debug=True)
