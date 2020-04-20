from flask import Flask,abort

app = Flask(__name__)


@app.route('/')
def index():
    10/0
    # 主动抛出异常  本质还是 raise，需要了解 __call__  方法
    return abort(403)


@app.errorhandler(403)
def error_handler(e):
    return "您访问的页面去浪迹天涯拉。。。%s"%e


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
