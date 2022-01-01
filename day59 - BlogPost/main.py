import re
from flask import Flask , render_template , request
import requests
import smtplib

MY_EMAIL = 'kevinlearningpython@gmail.com'
MY_PW = '5426233Kk!!'

app = Flask(__name__)

response = requests.get('https://api.npoint.io/379244e5f1ae236267d7')
blog_data = response.json()


@app.route('/')
def get_all_posts():
    return render_template('index.html', all_posts=blog_data)



@app.route('/about.html')
def about_me():
    return render_template('about.html')

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in blog_data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/contact.html', methods=['GET','POST'])
def receive_data():
    if request.method == 'GET':
        return render_template('contact.html', msg_sent=False)
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phoneNumber']
        message = request.form['message']
        with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PW)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f'Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone_number}\nMessage: {message}')
        return render_template('contact.html', msg_sent=True)

if __name__ == '__main__':
    app.run(debug=True)