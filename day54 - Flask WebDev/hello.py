from flask import Flask
import random

app = Flask(__name__)

num = random.choice(range(0,9))

@app.route("/")
def hello_world():
    return "<h1>Guess a number Between 0 and 9</h1><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route('/<int:number>')
def user_choice(number):
    global num
    if number > num:
        return "<h1 color=red;>TOO HIGH!</h1><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif number < num:
        return "<h1 color=blue;>TOO LOW!</h1><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 color=green;>FOUND YOU!!</h1><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
