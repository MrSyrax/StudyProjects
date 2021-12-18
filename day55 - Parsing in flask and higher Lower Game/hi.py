from flask import Flask

app = Flask(__name__)


def bold_decorator(function):
    def wf():
        text = function()
        return f'<b>{text}</b>'
    return wf

def em_decorator(function):
    def wf():
        text = function()
        return f'<em>{text}</b>'
    return wf

def under_decorator(function):
    def wf():
        text = function()
        return f'<u>{text}</u>'
    return wf



@app.route('/bye')
@bold_decorator
@em_decorator
@under_decorator
def bye():
    return 'Bye!'

if __name__ == '__main__':
    app.run(debug=True)