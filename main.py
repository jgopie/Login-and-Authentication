from flask import Flask, render_template, redirect, request
import smtplib
import os

app = Flask(__name__)

import Registration

if __name__ == "__main__":
    app.run(debug=True)
