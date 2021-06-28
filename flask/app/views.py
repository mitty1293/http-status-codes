from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:status_cd>')
def return_status_code(status_cd):
    pass

# 接続テスト用
@app.route('/test')
def test():
    return 'test OK.'