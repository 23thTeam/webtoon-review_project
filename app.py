from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import requests
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
    searchKeyword = db.Column(db.String, nullable=True)
    updateDays = db.Column(db.String, nullable=True)


with app.app_context():
    db.create_all()


@app.route("/webtoon/")
def webtoon():
    naver_api_url = "https://korea-webtoon-api.herokuapp.com/?perPage=20&service=naver"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

    def getWebtoonData(api_url):
        response = requests.get(api_url, headers=headers)
        return response.json()["webtoons"]

    context = {
        "naver": getWebtoonData(naver_api_url),
    }
    return render_template("webtoon.html", data=context)


@app.route('/user/')
def userhome():
    user_list = Webtoon.query.all()
    return render_template('user.html', data=user_list)


@app.route('/user/<webtoon_id>')
def webtoon_user(webtoon_id):
    web_user_list = Webtoon.query.filter_by(webtoon_id=webtoon_id).all()
    return render_template('user.html', data=web_user_list)


@app.route('/user/<username>')
def user(username):
    all_list = Webtoon.query.filter_by(username=username).all()
    return render_template('user.html', data=all_list)


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
    webtoon_title_receive = request.form.get("webtoon-title")
    webtoon_review_receive = request.form.get("review")

    webtoon = Webtoon(
        title=webtoon_title_receive,
        username=webtoon_username_receive,
        webtoon_id=webtoon_id_receive,
        author=webtoon_author_receive,
        url=webtoon_url_input_receive,
        img=webtoon_img_receive,
        service=webtoon_service_receive,
        fanCount=webtoon_fanCount_receive,
        searchKeyword=webtoon_searchKeyword_receive,
        updateDays=webtoon_updateDays_receive,
        webtoon_review=webtoon_review_receive,
    )

    db.session.add(webtoon)
    db.session.commit()

    return redirect(url_for("render_user_filter", username=webtoon_username_receive))


if __name__ == "__main__":
    app.run(debug=True)
