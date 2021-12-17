from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello,world"

@app.route("/bye")
def say_bye():
    return "Bye!"


@app.route("/username/<name>/1")
def greet(name):
    return f"hello there! {name+'12'} we are watching everyting you do!!!!!!"

if __name__ == "__main__":
    app.run(debug=True)
