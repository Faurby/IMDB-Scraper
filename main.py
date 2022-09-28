from urllib import request
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators, SubmitField
import os
import scrape

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()


class BasicForm(FlaskForm):
    seriesID = StringField('SeriesID', validators=[validators.input_required()])
    seasons = StringField('Seasons', validators=[validators.input_required()])
    submit = SubmitField("Submit")

@app.route("/", methods=['POST', 'GET'])
def index():
    form = BasicForm()
    searchString = ""
    seasons = 0
    data = ""
    if form.validate_on_submit():
        searchString = form.seriesID._value()
        seasons = form.seasons._value()
        data = scrape.getSeasonAverage(searchString, seasons)

    return render_template("index.html", form = form, data = data)
    
if __name__ == "__main__":
    app.run(debug=True)