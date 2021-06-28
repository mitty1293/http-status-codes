# http_status_codes
## 接続の流れ
1. ホストサーバー:8004/へ外部からアクセス
2. ホストサーバー:8004/ -> nginxコンテナ:80/ へマッピング
    * ref. docker-compose.yml/nginx/ports
3. nginxコンテナ:80/ -> flaskコンテナ:8000へリバースプロキシ
    * ref. default.conf
4. flaskコンテナ:8000 -> flaskアプリappへ接続
    * ref. docker-compose.yml/flask/command
## Reference
* https://qiita.com/mintak21/items/eeba4654a0db21abcb1c
* https://qiita.com/mintak21/items/d956389ee9338e6c0fe0
* https://docs.gunicorn.org/en/latest/settings.html
## Note
* 直接APサーバにつないでも良いがgunicornはwsgiサーバでありwebサーバではないので遅い。