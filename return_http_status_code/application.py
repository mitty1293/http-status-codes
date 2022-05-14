from http import HTTPStatus
from logging import basicConfig

from flask import Flask, Response, render_template

# Configure logging
basicConfig(
    filename="/app/logs/returnhttpstatuscode.log",
    format="%(asctime)s\t%(levelname)s\t%(filename)s\t%(module)s\tline:%(lineno)d\t%(message)s",
)

# Create an instance of the Flask application
app = Flask(__name__)


# Routing
@app.route("/")
def index():
    return render_template("index.html", status_lines=HTTPStatus)


@app.route("/<int:status_cd>")
def return_status_code(status_cd):
    if status_cd in [e.value for e in HTTPStatus]:
        return Response(
            response=f"{HTTPStatus(status_cd).value} {HTTPStatus(status_cd).phrase}",
            status=status_cd,
        )
    return Response(response=f"{status_cd} UNKNOWN", status=status_cd)
