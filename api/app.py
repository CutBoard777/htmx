from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/variable")
def var():
    user = "Geeksforgeeks"
    return render_template("variable_example.html", name=user)

@app.route("/for", methods=["POST", "GET"])
def for_loop():
    sex = request.form["sex"]
    count = sex + 1
    return render_template("for_example.html", count=count)

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="127.0.0.1")
