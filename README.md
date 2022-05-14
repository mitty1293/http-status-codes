# return-http-status-code
API to return HTTP status code
## Setup
Clone the repository
```
$ git clone https://github.com/mitty1293/return-http-status-code.git
```
Write the NGINX port to be accessed in the `return-http-status-code/.env` file.
```
NGINX_PORT=80
```
Start the container
```
$ docker-compose -f ./return-http-status-code/docker-compose.yml up -d
```
## Usage
Enter any status code in `[http_status_code]` and access the following URL.
```
http://host-ip:[NGINX_PORT]/[http_status_code]
```
If a status code that is not listed in the [class http.HTTPStatus](https://docs.python.org/3/library/http.html#http-status-codes) is specified, `404 Not Found` will be returned.
### Example
```Shell
$ curl -I http://host-ip:[NGINX_PORT]/500
HTTP/1.1 500 INTERNAL SERVER ERROR
Server: nginx/1.20.1
Date: Tue, 13 Jul 2021 15:16:34 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 0
Connection: keep-alive
```
## References
* https://httpstat.us/
* https://kamatimaru.hatenablog.com/entry/2021/07/05/231655
