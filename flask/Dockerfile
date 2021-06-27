FROM python:3.9.5-slim-buster

WORKDIR /usr/src

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# 何故かCMDではコンテナが起動しないが、commandでは起動する
# CMD ["/usr/local/bin/gunicorn", "-w", "2", "-b ", "0.0.0.0:8000", "app:app"]