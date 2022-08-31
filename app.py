from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

imgFolder = os.path.join("static", "images")

app.config["UPLOAD_FOLDER"] = imgFolder


@app.route("/", methods=["POST", "GET"])
def home_page():
    if request.method == "POST":
        return redirect("/BootStrap")
    showcase = os.path.join(app.config["UPLOAD_FOLDER"], "showcase.svg")
    fundamentals = os.path.join(app.config["UPLOAD_FOLDER"], "fundamentals.svg")

    return render_template("index.html", showcase=showcase, fundamentals=fundamentals)


@app.route("/BootStrap")
def project1():
    showcase = os.path.join(app.config["UPLOAD_FOLDER"], "showcase.svg")
    fundamentals = os.path.join(app.config["UPLOAD_FOLDER"], "fundamentals.svg")
    elon = os.path.join(app.config["UPLOAD_FOLDER"], "elon.webp")
    mark = os.path.join(app.config["UPLOAD_FOLDER"], "mark.jpg")
    david = os.path.join(app.config["UPLOAD_FOLDER"], "david.jpg")
    andrej = os.path.join(app.config["UPLOAD_FOLDER"], "andrej.jpg")
    react = os.path.join(app.config["UPLOAD_FOLDER"], "react.svg")
    la = os.path.join(app.config['UPLOAD_FOLDER'], "la.jpg")

    return render_template(
        "project1.html",
        showcase=showcase,
        fundamentals=fundamentals,
        elon=elon,
        mark=mark,
        david=david,
        andrej=andrej,
        react=react,
        la=la
    )
