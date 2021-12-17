from flask import Flask

app = Flask(__name__)

def bold_decorator(function):
    def wf():
        text = function()
        return f'<b>{text}</b>'
    return wf

def em_decorator(function):
    def wf():
        return f'<em>{function()}</em>'
    return wf

def under_decorator(function):
    def wf():
        return f'<u>{function()}</u>'
    return wf

@app.route("/")
@bold_decorator
@em_decorator
@under_decorator
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/<user>/<int:number>')
def user_number(user,number):
    return f'Hello {user}, you are number: {number}'

    
if __name__ == '__main__':
    app.run(debug=True)
