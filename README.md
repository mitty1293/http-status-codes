# return-http-status-code
API to return HTTP status code
## Setup
Start the container
```
# Production Environment
docker-compose -f docker-compose.prod.yml up -d

# Development Environment
docker-compose -f docker-compose.dev.yml up -d
```
## Usage
Enter any status code in `[http_status_code]` and access the following URL.
```
http://host-ip:8000/[http_status_code]
```
If a status code that is not listed in the [class http.HTTPStatus](https://docs.python.org/3/library/http.html#http-status-codes) is specified, `Unknown` will be returned.
### Example
```Shell
$ curl -I http://host-ip:8000/500
HTTP/1.1 500 INTERNAL SERVER ERROR
Server: nginx/1.20.1
Date: Tue, 13 Jul 2021 15:16:34 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 0
Connection: keep-alive
```
