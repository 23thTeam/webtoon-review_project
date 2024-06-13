from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class Webtoon(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = webtoon_id = db.Column(db.Integer, nullable=False)
    webtoon_id = db.Column(db.Integer, nullable=False)
    contents = db.Column(db.String, nullable=False)

    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)
    service = db.Column(db.String, nullable=False)

    updateDays = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'{self.artist} {self.title} 추천 by {self.username}'

with app.app_context():
    db.create_all()

@app.route('/')
def home():

    web_list = Webtoon.query.all()
    return render_template('home.html', data=web_list)

@app.route("/user_review/")
def user_review():
    webtoon_list = Webtoon.query.all()
    return render_template('user_review.html', data=webtoon_list)

@app.route("/user_review/<username>/")
def render_user_review_filter(username):
    filter_list = Webtoon.query.filter_by(webtoon_id=username).all()
    return render_template('user_review.html', data=filter_list)

@app.route("/webtoon/delete/")
def webtoon_delete():

    id_receive = request.args.get("id")

    song = db.session.get(Webtoon, id_receive)
    db.session.delete(song)
    db.session.commit()

    web_list = Webtoon.query.all()
    return render_template('home.html', data=web_list)

@app.route('/webtoon/create/')
def webtoon_create():

    title_receive = request.args.get("title")
    username_receive = request.args.get("username")
    webtoon_id_receive = request.args.get("webtoon_id")
    contents_receive = request.args.get("contents")
    webtoon = Webtoon(
                title=title_receive,
                username=username_receive,  
                webtoon_id=webtoon_id_receive,
                contents=contents_receive)
    db.session.add(webtoon)
    db.session.commit()
    
    web_list = Webtoon.query.all()
    return render_template('home.html', data=web_list)

if __name__ == '__main__':  
    app.run(debug=True)