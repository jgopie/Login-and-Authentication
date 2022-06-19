from flask import Flask
from flask_login import LoginManager
from datetime import timedelta

app = Flask(__name__)
app.config["SECRET_KEY"] = "454cc9133a0c32b0187199c9dff7328a71c5a2199494af48eeba0ad4d948781d"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=2)
login_manager = LoginManager()
login_manager.init_app(app)

import Registration
import Login_Logout
import Verification
import profile

if __name__ == "__main__":
    app.run(debug=True)
