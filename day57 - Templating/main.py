from logging import debug
from flask import Flask, render_template
import requests
from post import Post
from pprint import pprint

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/06534d22111e54a9bc8c").json()

post_objects = []
for post in posts:
    post_obj = Post(post['id'],post['subtitle'],post['title'],post['body'])
    post_objects.append(post_obj)

@app.route('/')
def home_page():
    return render_template('index.html', all_posts = post_objects)

@app.route('/post/<int:index>')
def get_blog(index):
    return render_template('post.html', post=post_objects[index])

if __name__ == '__main__':
    app.run(debug=True) 
