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
    username = db.Column(db.String(100), nullable=True)
    title = db.Column(db.String(100), nullable=True)


with app.app_context():
    db.create_all()


@app.route('/user/')
def home():
    api = "https://korea-webtoon-api.herokuapp.com"
    response = requests.get(api)
    rjson = response.json()['webtoons']
    context = {
        'webtoons': rjson,
    }
    return render_template('user.html', data=context)


@app.route('/user/<username>')
def render_user_filter(username):
    filter_list = Webtoon.query.filter_by(username=username).all()
    return render_template('user.html', data=filter_list)


def get_titles_by_username(username):
    data = Webtoon.query.filter_by(username=username).all()
    titles = [item.title for item in data]
    return jsonify({'username': username, 'titles': titles})


@app.route('/user/create/')
def home_create():
    id_receive = request.args.get('id')
    username_receive = request.args.get('username')
    title_receive = request.args.get('title')

    webtoon = Webtoon(
        id=id_receive, username=username_receive, title=title_receive)
    db.session.add(webtoon)
    db.session.commit()
    return redirect(url_for('render_user_filter', username=username_receive))


if __name__ == "__main__":
    app.run(debug=True)
