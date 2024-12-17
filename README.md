# return-http-status-code
API to return HTTP status code

Enter any HTTP status code in `[http_status_code]` and access https://returncode.fmitty.net/.  
Then you will get a response containing the code you specified.
```
https://returncode.fmitty.net/[http_status_code]
```

If a status code that is not listed in the [class http.HTTPStatus](https://docs.python.org/3/library/http.html#http-status-codes) is specified, `Unknown` will be returned.
## Example
```Shell
$ curl -I https://returncode.fmitty.net/500
HTTP/1.1 500 INTERNAL SERVER ERROR
Server: nginx/1.20.1
Date: Tue, 13 Jul 2021 15:16:34 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 0
Connection: keep-alive

$ curl -I https://returncode.fmitty.net/299
HTTP/1.1 299 UNKNOWN
Server: nginx/1.20.1
Date: Fri, 20 May 2022 13:14:42 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 11
Connection: keep-alive
```
## Self hosting
### Production Environment(via traefik)
Check the value of the HOST_DOMAIN environment variable for the host.
```
printenv HOST_DOMAIN
```
Start the container.
```
docker network create traefik_reverse_proxy_network
docker compose -f compose.traefik.yml up -d
```
Go to `https://returncode.${HOST_DOMAIN}/[http_status_code]`, you will get a response containing the code you specified.  

If you want to enable debug mode, change the environment variable `FLASK_DEBUG` in Dockerfile.
### Production Environment(Standalone)
Start the container.
```
docker compose -f compose.yml up -d
```
Go to `http://host-ip:8000/[http_status_code]`, you will get a response containing the code you specified.  

If you want to enable debug mode, change the environment variable `FLASK_DEBUG` in Dockerfile.  
If you want to change the port number, change the value in Dockerfile and compose file.
### Development Environment
Start the development server.
```
rye run devserver
```
Go to `http://host-ip:5000/[http_status_code]`.

## Test
```
rye test
```