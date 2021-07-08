# http-status-codes
API to return HTTP status code 
## 接続の流れ
1. ホストサーバー:8004/へ外部からアクセス
2. ホストサーバー:8004/ -> nginxコンテナ:80/ へマッピング
    * ref. docker-compose.yml/nginx/ports
3. nginxコンテナ:80/ -> flaskコンテナ:8000へリバースプロキシ
    * ref. default.conf
4. flaskコンテナ:8000 -> flaskアプリappへ接続
    * ref. docker-compose.yml/flask/command
## レスポンスの流れ
* `Response(status=xxx)` でステータスコードを格納したResponceオブジェクトを作成
* レスポンスボディは何も指定していないので空
* ステータスライン,レスポンスヘッダがレスポンスとして返される
## HTTPレスポンスメッセージの詳細
* レスポンスは上から3つに分かれる
    1. ステータスライン（便宜上ヘッダに含むことが多い）
    2. レスポンスヘッダ
    3. レスポンスボディ
```
HTTP/1.1 500 INTERNAL SERVER ERROR  ←ここがステータスライン
Server: nginx/1.20.1    ←ここから下がヘッダ
Date: Fri, 02 Jul 2021 06:39:04 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 0
Connection: keep-alive
.....   ←ここから下がボディ。今回は割愛。
```
* ステータスラインは3つに分かれる
    * プロトコル:`HTTP/1.1`
    * ステータスコード:`500`
    * ステータステキスト:`INTERNAL SERVER ERROR`
        * RFC7231 では Reason-Phrase と記載されている
## Reference
### Docker, Nginx, Gunicorn, Flask 環境設定
* https://qiita.com/mintak21/items/eeba4654a0db21abcb1c
* https://qiita.com/mintak21/items/d956389ee9338e6c0fe0
* https://docs.gunicorn.org/en/latest/settings.html
### HTTP Status Code
* [RFC7231 Section-6](https://datatracker.ietf.org/doc/html/rfc7231#section-6)
* [MDN Web Docs HTTPレスポンス](https://developer.mozilla.org/ja/docs/Web/HTTP/Messages#http_responses)
* http://ozuma.sakura.ne.jp/httpstatus/
* [HTTPステータスコード 完全に理解した](https://qiita.com/unsoluble_sugar/items/b080a16701946fcfce70)
### Flask Response
* [Werkzeug Reference class Response](https://werkzeug.palletsprojects.com/en/2.0.x/wrappers/#werkzeug.wrappers.Response)
* [flaskでhttpステータスを返却する方法](https://qiita.com/mink0212/items/52e0ebd66bd94e1303c1)
### Dictionary
* [不変な辞書を作成する](https://zenn.dev/sasano8/articles/python-006-dictionary#%E4%B8%8D%E5%A4%89%E3%81%AA%E8%BE%9E%E6%9B%B8%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B)
## Note
* 直接gunicornで立てたwebサーバにつないでも良いが、gunicornはnginxより遅いかも。
