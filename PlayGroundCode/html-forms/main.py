from logging import debug
from os import name
from types import MethodDescriptorType
from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def receive_data():
    name = request.form['fullname']
    password = request.form['pw']
    return f"<h1>Name:{name} pw:{password}</h1>"
    

if __name__ == '__main__':
    app.run(debug=True)