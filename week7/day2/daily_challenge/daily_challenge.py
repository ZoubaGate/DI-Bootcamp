from flask import *
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/green")
def green():
    return render_template("green.html")
@app.route("/yellow")
def yellow():
    return render_template("yellow.html")
@app.route("/red")
def red():
    return render_template("red.html")
@app.route("/blue")
def blue():
    return render_template("blue.html")
app.run()

