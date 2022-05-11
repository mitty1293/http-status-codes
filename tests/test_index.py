import pytest
from return_http_status_code.application import app


def test_index():
    app.config["TESTING"] = True
    rv = app.test_client().get("/")
    assert rv.status_code == 200
