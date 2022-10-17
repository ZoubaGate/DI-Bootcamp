from flask import Flask,render_template
import database_manager
app=Flask(__name__)

database_manager.create_database()

@app.route("/")
def home():
    return render_template("hello.html")

@app.route("/products")
def products_page():
    data = database_manager.load_database()
    # template_file=open('my_template.html','r').read()
    return render_template('listProducts.html',products=data)

@app.route("/product/<int:num>")
def detail(num):
    data = database_manager.load_database()
    # template_file=open('my_template.html','r').read()
    return render_template('detail.html',products=data,number=num)

if __name__=='__main__':
    app.run(debug=True,port=5000)
    
