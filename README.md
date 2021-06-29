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
### Docker, Nginx, Gunicorn, Flask
* https://qiita.com/mintak21/items/eeba4654a0db21abcb1c
* https://qiita.com/mintak21/items/d956389ee9338e6c0fe0
* https://docs.gunicorn.org/en/latest/settings.html
### HTTP Status Code
* http://ozuma.sakura.ne.jp/httpstatus/
* https://qiita.com/mink0212/items/52e0ebd66bd94e1303c1
### Dictionary
* [不変な辞書を作成する](https://zenn.dev/sasano8/articles/python-006-dictionary#%E4%B8%8D%E5%A4%89%E3%81%AA%E8%BE%9E%E6%9B%B8%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B)
## Note
* 直接APサーバにつないでも良いがgunicornはwsgiサーバでありwebサーバではないので遅い。