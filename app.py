from flask import Flask, render_template, request, url_for, redirect
import requests

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
    webtoon_review = db.Column(db.String, nullable=False)
    webtoon_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)
    service = db.Column(db.String, nullable=False)
    fanCount = db.Column(db.String, nullable=False)
    searchKeyword =  db.Column(db.String, nullable=False) 
    updateDays = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'{self.title} {self.author} 추천 by {self.username}'


with app.app_context():
    db.create_all()


@app.route('/') # 홈으로 설정
def home():
    return render_template("home.html")

@app.route('/user/')
def user():
    data_list = Webtoon.query.all()
    return render_template('user.html', data=data_list)

@app.route('/user/<username>')
def render_user_filter(username):
    filter_list = Webtoon.query.filter_by(username=username).all()
    return render_template('user.html', data=filter_list)

@app.route("/webtoon/", methods=['GET', 'POST'])
def webtoon():
    # 웹툰 API 받아오기
    # naver_api_url = "https://korea-webtoon-api.herokuapp.com/?perPage=20&service=naver"
    naver_api_url = "https://korea-webtoon-api.herokuapp.com/?perPage=50&service=naver"
    kakao_api_url = "https://korea-webtoon-api.herokuapp.com/?perPage=50&service=kakao"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

    def getWebtoonData(api_url):
        response = requests.get(api_url, headers=headers)
        return response.json()["webtoons"]

    context = {
        "naver": getWebtoonData(naver_api_url),
        "kakao": getWebtoonData(kakao_api_url),
    }
    
    # 검색 시 GET 사용할 경우 혼동 생기므로 
    # POST 로 받아 서치로 리디렉션 먼저하기
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        return redirect(url_for('search', keyword=keyword))

    return render_template("webtoon.html", data=context)


@app.route("/webtoon/search")
def search():
    # GET 메소드로 검색 결과 받아오기
    keyword = request.args.get('keyword')

    # keyword 있으면 웹툰 API 받아오기
    if keyword:
        search_api_url = f"https://korea-webtoon-api.herokuapp.com/search?keyword={keyword}"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
        response = requests.get(search_api_url, headers=headers)
        webtoons = response.json()["webtoons"]
        context = {
            "webtoons" : webtoons,
            "keyword": keyword,
        }

        return render_template("search.html", data=context)
    # 키워드 없으면 원래대로 리디렉션
    else:
        return redirect(url_for('webtoon'))


@app.route("/webtoon/<webtoon_id>")
def webtoonDetail(webtoon_id):

    # 웹툰 하나하나 가져오는 api
    # naver_api_url = "https://korea-webtoon-api.herokuapp.com/?perPage=20&service=naver"
    api_url = "https://korea-webtoon-api.herokuapp.com/?perPage=100"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
    response = requests.get(api_url, headers=headers)

    # 해당 웹툰에 대한 리뷰 데이터를 db에서 가져오는 곳
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
    # Webtoon.query.filter_by(webtoonId=int(webtoon_id)).all()

    # api 데이를 순회해서 id 같은 웹툰 찾기

    if response.status_code == 200:
        webtoons = response.json().get("webtoons", [])
        webtoon_detail = next((webtoon for webtoon in webtoons if int(webtoon['webtoonId']) == int(webtoon_id)), None)
    else:
        webtoon_detail = None

    # 웹툰 데이터, 웹툰 리뷰 데이터

    data = {
        "webtoon_detail": webtoon_detail,
        "webtoon_review_list": webtoon_review_list,
    }

    return render_template("webtoonDetail.html", data=data)


@app.route("/webtoon/create", methods=["POST"])
def webtoonCreate():
    webtoon_username_receive = request.form.get("username")
    webtoon_id_receive = request.form.get("webtoon-id")
    webtoon_author_receive = request.form.get("webtoon-author")
    webtoon_url_input_receive = request.form.get("webtoon-url-input")
    webtoon_img_receive = request.form.get("webtoon-img")
    webtoon_service_receive = request.form.get("webtoon-service")
    webtoon_fanCount_receive = request.form.get("webtoon-fanCount")
    webtoon_searchKeyword_receive = request.form.get("webtoon-searchKeyword")
    webtoon_updateDays_receive = request.form.get("webtoon-updateDays")
    webtoon_title_receive=request.form.get("webtoon-title")
    webtoon_review_receive=request.form.get("review")

    webtoon = Webtoon(
                title=webtoon_title_receive,
                username=webtoon_username_receive,  
                webtoon_id=webtoon_id_receive,
                author=webtoon_author_receive,
                url= webtoon_url_input_receive,
                img = webtoon_img_receive,
                service = webtoon_service_receive,
                fanCount = webtoon_fanCount_receive,
                searchKeyword = webtoon_searchKeyword_receive,
                updateDays = webtoon_updateDays_receive,
                webtoon_review = webtoon_review_receive,
                )

    db.session.add(webtoon)
    db.session.commit()

    return redirect(url_for("render_user_filter",username=webtoon_username_receive))

@app.route("/webtoon/delete/")
def webtoon_delete():

    id_receive = request.args.get("id")

    data = db.session.get(Webtoon, id_receive)
    db.session.delete(data)
    db.session.commit()

    webtoon_list = Webtoon.query.all()
    return render_template('user.html', data=webtoon_list)

if __name__ == "__main__":
    app.run(debug=True , port=5000)