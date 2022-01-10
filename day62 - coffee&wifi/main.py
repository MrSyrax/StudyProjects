from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import wtforms
from wtforms.validators import DataRequired, URL
import csv
from pprint import pprint
import os
from choices import wifi_strength, coffee_strength, power_outlets

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    Cafe_location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(),URL()])
    Cafe_open = StringField('Opening Time e.g 8AM', validators=[DataRequired()])
    Cafe_close = StringField('Closing Time e.g 5PM', validators=[DataRequired()])
    Cafe_wifi_strength = wtforms.SelectField('Wifi Strength Rating', choices=wifi_strength, validators=[DataRequired()])
    coffee_strength = wtforms.SelectField('Coffee Rating', choices=coffee_strength, validators=[DataRequired()])
    power_sockets = wtforms.SelectField('Power Socket Availability', choices=power_outlets, validators=[DataRequired()])

    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        path = 'C:/Users/karey/Documents/Python/day62 - coffee&wifi/cafe-data.csv'
        my_dict = [form.cafe.data,form.Cafe_location.data,form.Cafe_open.data,form.Cafe_close.data,form.coffee_strength.data,form.Cafe_wifi_strength.data,form.power_sockets.data]
        with open(path , 'a' , newline='',encoding='utf-8') as csv_file:
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow(my_dict)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('C:/Users/karey/Documents/Python/day62 - coffee&wifi/cafe-data.csv', newline='',encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)