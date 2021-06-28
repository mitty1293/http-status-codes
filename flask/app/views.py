from app import app

@app.route('/<int:status_cd>')
def return_status_code:
    pass

# 接続テスト用
@app.route('/test')
def test():
    return 'test OK.'