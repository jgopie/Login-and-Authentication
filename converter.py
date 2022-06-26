from __main__ import app
from flask import Flask, render_template, request, flash, redirect, send_file
from werkzeug.utils import secure_filename
import os
import pandas as pd
from fpdf import FPDF
import io

UPLOAD_FOLDER = "static/files"
ALLOWED_EXTENSIONS = {"csv"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/converter", methods=["GET", "POST"])
def converter():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No File Selected")
            return render_template("converter.html")
        file = request.files["file"]
        if file.filename == "":
            flash("No File Selected")
            return render_template("converter.html")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return render_template("success.html", name=filename)
    return render_template("converter.html")


@app.route("/display", methods=["GET", "POST"])
def success():
    if request.method == "POST":
        data = pd.read_csv(f"static/files/{request.form['file']}")
        pdf = FPDF()
        for i in range(0, len(data.index)):
            pdf.add_page()
            pdf.set_font("Times", "B", 12)
            pdf.cell(100, 10, f"Delivery ID: {data.iloc[i]['Delivery ID']}", border=1, align="left", ln=1)
            pdf.cell(100, 10, f"Customer Name: {data.iloc[i]['Customer Name']}", border=1, align="left", ln=1)
            pdf.cell(100, 10, f"Address: {data.iloc[i]['Address']}", border=1, align="left", ln=1)
            pdf.cell(100, 10, f"Delivery Instructions: {data.iloc[i]['Delivery Instructions']}", border=1, align="left",
                     ln=1)
            pdf.cell(100, 10, f"Contact Information: {data.iloc[i]['Contact Information']}", border=1, align="left",
                     ln=1)
        pdf.output(f"test.pdf", "F")
        stream = io.BytesIO(pdf.output(dest='S').encode('latin-1'))
        return send_file(stream, mimetype="application/pdf", as_attachment=False)
