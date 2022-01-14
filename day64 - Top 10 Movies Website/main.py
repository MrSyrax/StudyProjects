from datetime import timedelta
from flask import Flask, render_template, redirect, url_for, request
from flask.scaffold import F
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
import sqlalchemy
from sqlalchemy.util.langhelpers import method_is_overridden
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from pprint import pprint

#Initial Setup
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-10-movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)
API_URL = 'https://api.themoviedb.org/3/search/movie'
API_URL_ID = 'https://api.themoviedb.org/3/movie'
MOVIE_DB_IMAGE = "https://image.tmdb.org/t/p/w500"
API_KEY = '7ad4cdc53c3b7f891b22fb19c6070d7d'

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

db.create_all()

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    movie_title = StringField("Movie Title")
    submit = SubmitField("Done")

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating.desc()).all()
    return render_template("index.html" , all_movies = all_movies)


@app.route('/edit', methods=['GET','POST'])
def edit():
    form = RateMovieForm()
    movie_id= request.args.get('id')
    movie_to_edit = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_to_edit.rating = float(form.rating.data)
        movie_to_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie = movie_to_edit , form=form)

@app.route('/delete', methods=['GET','POST'])
def delete():
    id = request.args.get('id')
    movie_to_delete = Movie.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET','POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_to_search = {
            'api_key':API_KEY,
            'query': form.movie_title.data
            }
        response = requests.get(API_URL, params=movie_to_search)
        data = response.json()['results']
        return render_template('select.html', options=data)
    return render_template('add.html', form=form)

@app.route('/find')
def find():
    movie_api_id = request.args.get('id')
    print(movie_api_id)
    if movie_api_id:
        movie_api_url = f'{API_URL_ID}/{movie_api_id}'
        response = requests.get(movie_api_url, params={"api_key":API_KEY, "include_adult":"True","language":"en-US"})
        data = response.json()
        new_movie = Movie(
            title = data['original_title'],
            year = data['release_date'].split('-')[0],
            description = data['overview'],
            rating = data['vote_average'],
            review = ' ',
            img_url = f"{MOVIE_DB_IMAGE}/{data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
