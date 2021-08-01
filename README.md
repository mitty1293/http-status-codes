# return-http-status-code
API to return HTTP status code
## Setup
```
$ git clone https://github.com/mitty1293/return-http-status-code.git
$ docker-compose -f ./return-http-status-code/docker-compose.yml up -d
```
## Usage
Enter any status code in `[http_status_code]` and access the following URL.
```
http://host-ip:8004/[http_status_code]
```
If a status code that is not listed in the `flask/app/const.py` is specified, `404 Not Found` will be returned.
### Example
```Shell
$ curl -I http://host-ip:8004/500
HTTP/1.1 500 INTERNAL SERVER ERROR
Server: nginx/1.20.1
Date: Tue, 13 Jul 2021 15:16:34 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 0
Connection: keep-alive
```
