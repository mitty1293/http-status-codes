from http import HTTPStatus
from app import app
from flask import render_template, Response

@app.route('/')
def index():
    return render_template("index.html", status_lines=HTTPStatus)

@app.route('/<int:status_cd>')
def return_status_code(status_cd):
    if status_cd in [e.value for e in HTTPStatus]:
        return Response(status=status_cd)
    return Response(status=404)

# connection test
@app.route('/test')
def test():
    return 'test OK.'
