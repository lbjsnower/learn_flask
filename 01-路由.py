from flask import Flask

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])  # 必须以路径分隔符 / 开头
def index():
    return 'hello world'


if __name__ == '__main__':
    # 保存了该应用页面所有的 路由规则
    print('=====================')

    print(app.url_map)
    """
    Map([<Rule '/' (GET, HEAD, OPTIONS) -> index>,
    <Rule '/static/<filename>' (GET, HEAD, OPTIONS) -> static>])
    """
    print('=====================')
    app.run(host='0.0.0.0', port=5000, debug=True)
