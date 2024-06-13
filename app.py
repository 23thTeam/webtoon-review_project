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
    webtoon_review = db.Column(db.String, nullable=True)

    title = db.Column(db.String, nullable=True)
    author = db.Column(db.String, nullable=True)
    url = db.Column(db.String, nullable=True)
    img = db.Column(db.String, nullable=True)
    service = db.Column(db.String, nullable=True)

    fanCount = db.Column(db.String, nullable=True)
    searchKeyword =  db.Column(db.String, nullable=True) 
    updateDays = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f'{self.artist} {self.title} 추천 by {self.username}'

with app.app_context():
    db.create_all()

@app.route('/')
def home():

    res = requests.get(
	"https://korea-webtoon-api.herokuapp.com/?perPage=20"
    )
    rjson = res.json()
    webtoon_list = rjson["webtoons"]

    for webtoon in webtoon_list:

        username_receive = ""
        webtoon_review_receive = ""

        webtoon_id_receive = webtoon['webtoonId']   
        title_receive = webtoon['title']
        author_receive = webtoon['author']
        url_receive = webtoon['url']
        img_receive = webtoon['img']
        service_receive = webtoon['service']
        fanCount_receive = webtoon['fanCount']
        searchKeyword_receive = webtoon['searchKeyword']

        updateDays_receive = webtoon['updateDays'][0]

        web = Webtoon(webtoon_id=webtoon_id_receive,
                      username = username_receive,
                      webtoon_review = webtoon_review_receive,
                      title=title_receive,
                      author=author_receive,
                      url=url_receive,
                      img=img_receive,
                      service=service_receive,
                      fanCount=fanCount_receive,
                      searchKeyword=searchKeyword_receive,
                      updateDays=updateDays_receive)
        db.session.add(web)
        db.session.commit()

    web_list = Webtoon.query.all()
    return render_template('home.html', data=web_list)

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