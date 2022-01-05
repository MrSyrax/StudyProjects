from flask import Flask , render_template , request
from flask.scaffold import F
import requests
from pprint import pprint
import smtplib
from decouple import config

MY_EMAIL = config('MY_USER')
MY_PW = config('MY_PW')


response = requests.get('https://api.npoint.io/5523eaa1e4950c2d9bcd')
blog_posts = response.json()

app = Flask(__name__)

@app.route('/')
def home_posts():
    return render_template('index.html', all_posts=blog_posts)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact_page():
    if request.method == 'GET':
        return render_template('contact.html', msg_sent=False)
    elif request.method == 'POST':
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            name = request.form['name']
            email = request.form['email']
            phone_number = request.form['phoneNumber']
            message = request.form['message']
            connection.starttls()
            connection.login(MY_EMAIL,MY_PW)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f'Subject:New Message\n\nName:{name}\nEmail: {email}\nPhone Number: {phone_number}\nMessage: {message}')
        return render_template('contact.html', msg_sent=True)

@app.route('/post/<int:index>')
def get_single_post(index):
    requested_post = None
    for post in blog_posts:
         if post['id'] == index:
            requested_post = post
            return render_template('post.html', post=requested_post)

if __name__ == '__main__':
    app.run(debug=True)