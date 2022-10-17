import flask_wtf
import wtforms
from flask import *
import json

app = Flask(__name__)



list_of_cities=[]
@app.route('/', methods=["GET","POST"])
def myform():
    # form = Form()
    if request.method=='POST': # Check if the form has been filled
        infoCity={}
        
        infoCity['nameCity']=request.form['nameCity']
        infoCity['country']=request.form['nameCountry']
        infoCity['numberInhabitants']=request.form['numberInhabitants']
        infoCity['cityArea']=request.form['cityArea']
        
        list_of_cities.append(infoCity)
        with open('city.json', 'w') as file_obj:
            json.dump(list_of_cities, file_obj)

        
    return render_template("form.html")

def load_database(src_file='city.json'):
    with open(src_file, 'r') as file_obj:
        data = json.load(file_obj)
    return data

app.run()
