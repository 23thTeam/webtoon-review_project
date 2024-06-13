from flask import Flask, render_template, request, url_for, redirect
import requests

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
    username = webtoon_id = db.Column(db.String, nullable=False)
    webtoon_review = db.Column(db.String, nullable=True)
    webtoon_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=True)
    author = db.Column(db.String, nullable=True)
    url = db.Column(db.String, nullable=True)
    img = db.Column(db.String, nullable=True)
    service = db.Column(db.String, nullable=True)
    fanCount = db.Column(db.String, nullable=True)
    searchKeyword =  db.Column(db.String, nullable=True) 
    updateDays = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f'{self.title} {self.author} 추천 by {self.username}'

with app.app_context():
    db.create_all()



@app.route('/') # 홈으로 설정
def home():
    return render_template("home.html")


@app.route("/webtoon/")
def webtoon():
    naver_api_url = "https://korea-webtoon-api.herokuapp.com/?perPage=20&service=naver"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

    def getWebtoonData(api_url):
        response = requests.get(api_url, headers=headers)
        return response.json()["webtoons"]

    context = {
        "naver": getWebtoonData(naver_api_url),
    }    
    return render_template("webtoon.html", data=context)


@app.route("/webtoon/<webtoon_id>")
def webtoonDetail(webtoon_id):
    api_url = "https://korea-webtoon-api.herokuapp.com/?perPage=20&service=naver"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
    response = requests.get(api_url, headers=headers)

    # 테스트용 데이터
    webtoon_review_list =  []
    review1 = {
       'username': '유저 이름',
        'title': '리뷰 제목',
        'text': '리뷰 텍스트 리뷰 텍스트 리뷰 텍스트 테스트'
    }
    webtoon_review_list.append(review1)
    webtoon_review_list.append(review1)
    webtoon_review_list.append(review1)
    webtoon_review_list.append(review1)
    webtoon_review_list.append(review1)
    webtoon_review_list.append(review1)
    webtoon_review_list.append(review1)

    # 리뷰 데이터: webtoon_id 필터해서 가져오기
    # Review.query.filter_by(webtoonId=int(webtoon_id)).all()

    if response.status_code == 200:
        webtoons = response.json().get("webtoons", [])
        webtoon_detail = next((webtoon for webtoon in webtoons if int(webtoon['webtoonId']) == int(webtoon_id)), None)
    else:
        webtoon_detail = None

    data = {
        "webtoon_detail": webtoon_detail,
        "webtoon_review_list": webtoon_review_list,
    }
    
    return render_template("webtoonDetail.html", data=data)


if __name__ == "__main__":
    app.run(debug=True , port=5000)
