# http_status_codes
* 直接APサーバにつないでも良いが、gunicornはwsgiサーバでありwebサーバではないので遅い。
## 接続の流れ
1. ホストサーバー:8004/へ外部からアクセス
2. ホストサーバー:8004/ -> nginxコンテナ:80/ へマッピング
    * ref. docker-compose.yml/nginx/ports
3. nginxコンテナ:80/ -> flaskコンテナ:8000へリバースプロキシ
    * ref. default.conf
4. flaskコンテナ:8000 -> flaskアプリappへ接続
    * ref. docker-compose.yml/flask/command
