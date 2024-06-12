from flask import Flask, render_template, request, url_for, redirect
import requests
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DB
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

# class Review(db.Model)
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), nullable=False)
#     webtoonId =  db.Column(db.Integer, nullable=False)
#     title = db.Column(db.String(100), nullable=False)
#     text = db.Column(db.String(1000), nullable=False)

#     def __repr__(self):
#         return f'{self.title} {self.text} 추천 by {self.username}'

with app.app_context():
    db.create_all()


# 테스트 용으로 작성

# @app.route("/")
# def home():
#     api_url = "https://korea-webtoon-api.herokuapp.com/?perPage=20&service=naver"
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
#     response = requests.get(api_url, headers=headers)
#     webtoons = response.json()["webtoons"]

#     return render_template("home.html", data=webtoons)



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
