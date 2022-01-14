from enum import unique
from types import MethodDescriptorType
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///owned-rc-cars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chassis = db.Column(db.String(250), nullable=False)
    used_for = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<Cars{self.chassis}>'

db.create_all()

@app.route('/', methods=['GET','POST'])
def home():
    list_of_cars = db.session.query(Cars).all()
    return render_template('index.html', all_cars = list_of_cars)


@app.route("/add", methods=['GET','POST'])
def add():
    if request.method=='POST':
        new_chassis = request.form['chassis']
        new_use = request.form['use']
        new_rating = request.form['rating']
        new_car = Cars(chassis=new_chassis,used_for=new_use,rating=new_rating)
        db.session.add(new_car)
        db.session.commit()
    return render_template('add.html')

@app.route('/edit', methods=['GET','POST'])
def edit_rating():
    if request.method=='POST':
        car_id = request.form['id']
        car_to_edit = Cars.query.get(car_id)
        car_to_edit.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    car_id = request.args.get('id')
    print(car_id)
    car_to_edit = Cars.query.get(car_id)
    return render_template('edit.html', car_rating=car_to_edit)


@app.route('/delete', methods=['GET','POST'])
def delete():
    car_id = request.args.get('id')
    car_to_delete = Cars.query.get(car_id)
    db.session.delete(car_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True) 