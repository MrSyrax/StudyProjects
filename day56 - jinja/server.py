from math import perm
from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    date = datetime.now()
    year = date.year
    random_number = random.randint(1,10)
    return render_template('index.html', num=random_number, foot=year)

@app.route('/guess/<name>')
def guess_name(name):
    response = requests.get(f'https://api.genderize.io?name={name}')
    response2 = requests.get(f'https://api.agify.io?name={name}')
    answer2 = response2.json()
    answer = response.json()
    age = answer2['age']
    gender = answer['gender']
    return render_template('random.html', age=age, name_answer=name.title() ,gender=gender )

@app.route('/blog/<int:num>')
def blog_posts(num):
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts, num=num)

if __name__ == '__main__':
    app.run(debug=True)
