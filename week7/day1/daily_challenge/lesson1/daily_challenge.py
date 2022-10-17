from flask import *
app=Flask(__name__)

@app.route("/in-this-chapter.md")
def cour():
    return render_template("in-this-chapter.md")

@app.route("/exercices.md")
def exercice():
    return render_template("exercises.md")

if __name__=='__main__':
    app.run(debug = True)