from flask import Flask, render_template, redirect, url_for, request
import math

app = Flask(__name__)

timer = 0
hue = 0



@app.route("/")
def home():
    global timer
    timer = 0
    return render_template("index.html")

@app.route("/mouse_entered", methods=["POST", "GET"])
def moyse_entered():
    return render_template("mouse_entered.html")

@app.route("/buton", methods=["POST", "GET"])
def buton():
    return render_template("buton.html")

@app.route("/clicked", methods=["POST", "GET"])
def clicked():
    return render_template("clicked.html")

@app.route("/timer", methods=["POST", "GET"])
def time():
    global timer
    timer += 1
    return render_template("timer.html", timer=timer)

@app.route("/colors", methods=["POST", "GET"])
def colors():
    global hue
    hue = (hue+60) %360
    return render_template("colors.html", hue=hue)

@app.route("/sigma", methods=["POST", "GET"])
def sigma():
    return render_template("sigma.html")

@app.route("/agmis", methods=["POST", "GET"])
def agmis():
    return render_template("agmis.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")
