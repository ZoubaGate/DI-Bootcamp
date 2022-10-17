from flask import *
from random import randint
app = Flask(__name__)

@app.route('/')
def myview():
    x = input("write a number between 1 and 100: ")
    roll = randint(1,100)
    if x==roll:
        return 'you are genie'
    else:
        return 'you lost'
  
 
if __name__ =='__main__':
    app.run(debug = True) 
    