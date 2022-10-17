from flask import *

app = Flask(__name__)
listCv={}
@app.route("/",methods=['GET','POST'])
def mycv():
    if request.method=='POST':
        listCv['firstname']=request.form['firstname']
        listCv['lastname']=request.form['lastname']
        listCv['age']=request.form['age']
        listCv['experience']=request.form['experience']
        
        return redirect("/afficheCv")
    return render_template("mycv.html")

@app.route("/afficheCv")
def afficheCv():
    return render_template("afficheCv.html",liste=listCv)

if __name__=='__main__':
    app.run()
