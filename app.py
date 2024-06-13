from flask import Flask, render_template, request, url_for, redirect, jsonify
import requests

import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    review = db.Column(db.String, nullable=False)
    webtoon_id = db.Column(db.Integer, nullable=False)
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "review": self.review,
            "webtoon_id": self.webtoon_id,
        }

    # ✅ 같은 유저가 동일한 웹툰에 대해 중복된 리뷰를 작성하는 것을 방지
    # __table_args__ = (db.UniqueConstraint('username', 'webtoon_id', name='unique_user_webtoon_review'),)

    # # 디비 확인 위해 디버깅/로그 기록
    # def __repr__(self):
    #     return f'review by {self.username} for webtoon_id: {self.webtoon_id}'
    
class Webtoon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    webtoon_id = db.Column(db.Integer, nullable=False, unique=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)
    service = db.Column(db.String, nullable=False)
    update_days = db.Column(db.String, nullable=True) # 없는 것도 있음
    fan_count = db.Column(db.Integer, nullable=True) # 없는 것도 있음
    search_keyword =  db.Column(db.String, nullable=False) 

    def to_dict(self):
        return {
            "id": self.id,
            "webtoon_id": self.webtoon_id,
            "title": self.title,
            "author": self.author,
            "url": self.url,
            "img": self.img,
            "service": self.service,
            "update_days": self.update_days,
            "fan_count": self.fan_count,
            "search_keyword": self.search_keyword
        }
    
# ✅ 서버 시작 전 이미 생성해 뒀기 때문에 빼도 될거 같음
# ✅ 프로덕션 환경에선 빼도 된다고 하는데 확인 필요
# with app.app_context():
#     db.create_all()


@app.route('/') # 홈으로 설정
def home():
    return render_template("home.html")

@app.route('/user')
def user():
    data_list = Review.query.all()
    return render_template('user.html', data=data_list)

@app.route('/user/<username>')
def render_user_filter(username):
    filter_list = Review.query.filter_by(username=username).all()
    return render_template('user.html', data=filter_list)


@app.route("/webtoon", methods=['GET', 'POST'])
def webtoon():
    # context = {
    #     "naver": get_by_service_webtoon_db(service="naver"),
    #     "kakao": get_by_service_webtoon_db(service="kakao"),
    #     "kakaoPage": get_by_service_webtoon_db(service="kakaoPage"),
    # }
    
    kakao = db.session.query(Webtoon).filter_by(service="kakao").all()
    webtoon_list = [webtoon.to_dict() for webtoon in kakao]
    
    # 검색 시 GET 사용할 경우 혼동 생기므로, POST 로 받아 서치로 리디렉션 먼저하기
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        return redirect(url_for('search', keyword=keyword))

    return render_template("webtoon.html", data=webtoon_list)


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
    # Review.query.filter_by(webtoon_id=int(webtoon_id)).all()

    # api 데이를 순회해서 id 같은 웹툰 찾기
    webtoons = response.json().get("webtoons", [])
    webtoon_detail = next((webtoon for webtoon in webtoons if int(webtoon['webtoon_id']) == int(webtoon_id)), None)


    # 웹툰 데이터, 웹툰 리뷰 데이터
    data = {
        "webtoon_detail": webtoon_detail,
        "webtoon_review_list": webtoon_review_list,
    }

    return render_template("webtoonDetail.html", data=data)


@app.route("/webtoon/create", methods=["POST"])
def webtoonCreate():
    webtoon_username_receive = request.form.get("username")
    webtoon_review_receive=request.form.get("review")
    webtoon_id_receive = request.form.get("webtoon-id")

    webtoon = Review(
                username=webtoon_username_receive,  
                review=webtoon_review_receive,
                webtoon_id=webtoon_id_receive,
                )

    db.session.add(webtoon)
    db.session.commit()

    return redirect(url_for("render_user_filter",username=webtoon_username_receive))


# ✅ 엔드포인트 바꿔야 할것 같아요 웹툰을 삭제하는게 아니라 리뷰를 삭제하는 거니까
@app.route("/webtoon/delete/")
def webtoon_delete():
    id_receive = request.args.get("id")

    data = db.session.get(Webtoon, id_receive)
    db.session.delete(data)
    db.session.commit()

    webtoon_list = Review.query.all()
    return render_template('user.html', data=webtoon_list)

if __name__ == "__main__":
    app.run(debug=True , port=5000)




# data = [
#     {
#         '_id': '63821f5724614f7fb3c99267', 
#         'webtoon_id': 1000000797153, 
#         'title': '일진담당일진', 
#         'author': 'GRIMZO', 
#         'url': 'https://m.comic.naver.com/webtoon/list?titleId=797153&week=dailyPlus',
#         'img': 'https://image-comic.pstatic.net/webtoon/797153/thumbnail/thumbnail_IMAG21_62fa8e3d-e445-4dd4-9730-88364faa18e0.jpg',
#         'service': 'naver',
#         'updateDays': ['naverDaily'],
#         'fanCount': 50,
#         'searchKeyword': '일진담당일진grimzo',
#         'additional': {'new': False, 'adult': False, 'rest': False, 'up': False, 'singularityList': ['waitFree']}
#         }, { ... }, ... ]