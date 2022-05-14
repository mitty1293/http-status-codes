from http import HTTPStatus

import pytest
from return_http_status_code.application import app

valid_httpstatus = [e.value for e in HTTPStatus]
invalid_httpstatus = list(set([i for i in range(200, 600)]) - set(valid_httpstatus))


@pytest.mark.parametrize("status_cd", valid_httpstatus)
def test_return_status_code_validstatus(status_cd):
    app.config["TESTING"] = True
    rv = app.test_client().get(f"/{status_cd}")
    assert status_cd == rv.status_code
    assert f"{HTTPStatus(status_cd).phrase}" in rv.data.decode()


@pytest.mark.parametrize("status_cd", invalid_httpstatus)
def test_return_status_code_invalidstatus(status_cd):
    app.config["TESTING"] = True
    rv = app.test_client().get(f"/{status_cd}")
    assert status_cd == rv.status_code
    assert "Non-standard Code" in rv.data.decode()
