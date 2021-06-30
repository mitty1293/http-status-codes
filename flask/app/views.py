from app import app
from flask import render_template, Response
#from const import HTTPStatusCode
# -------------------------------
from types import MappingProxyType

class HTTPStatusCode():
    def __init__(self):
            self.status_line = MappingProxyType({
                200:"OK",
                403:"Forbidden",
                404:"Not Found",
                500:"Internal Server Error"
            })
#--------------------------------

responce = HTTPStatusCode()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:status_cd>')
def return_status_code(status_cd):
    if status_cd in responce.status_line.keys():
        return Response(status=status_cd)
    else:
        return Response(status=404)

# connection test
@app.route('/test')
def test():
    return 'test OK.'