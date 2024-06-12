from flask import Flask, render_template
import os
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# 포트 8080으로 설정함
if __name__ == "__main__":
    app.run(debug=True , port=5000)
