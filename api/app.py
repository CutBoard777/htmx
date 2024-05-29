from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
strength = 1
sex = 0
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/variable")
def var():
    user = "Geeksforgeeks"
    return render_template("variable_example.html", name=user)

@app.route("/clicked", methods=["POST", "GET"])
def for_loop():
    global sex
    global strength
    sex = sex + strength
    return render_template("for_example.html", sex=sex)

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="127.0.0.1")
