ARG PYTHON_VERSION=3.12

FROM python:${PYTHON_VERSION}

RUN pip install uv

WORKDIR /opt
COPY requirements.lock ./
RUN uv pip install --no-cache --system -r requirements.lock

COPY src .
ENV FLASK_DEBUG=False
CMD ["sh", "-c", "/usr/local/bin/gunicorn --bind 0.0.0.0:8000 --workers 2 --timeout 60 return_http_status_code.application:app"]