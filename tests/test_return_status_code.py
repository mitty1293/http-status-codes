from http import HTTPStatus

import pytest
from return_http_status_code.application import app

valid_httpstatus = [e.value for e in HTTPStatus]
invalid_httpstatus = list(set([i for i in range(100, 600)]) - set(valid_httpstatus))


@pytest.mark.parametrize("status_cd", valid_httpstatus)
def test_return_status_code_valid_httpstatus(status_cd):
    app.config["TESTING"] = True
    rv = app.test_client().get(f"/{status_cd}")
    assert status_cd == rv.status_code
    # Response with body or Response with empty body(100, 101, 102, 103, 204, 304)
    assert (
        f"{HTTPStatus(status_cd).phrase}" in rv.data.decode() or "" == rv.data.decode()
    )


@pytest.mark.parametrize("status_cd", invalid_httpstatus)
def test_return_status_code_invalid_httpstatus(status_cd):
    app.config["TESTING"] = True
    rv = app.test_client().get(f"/{status_cd}")
    assert status_cd == rv.status_code
    # Response with body or Response with empty body(100-199)
    assert "Unknown" in rv.data.decode() or "UNKNOWN" in rv.status
