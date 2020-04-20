import json

from flask import Flask, make_response, Response, jsonify, redirect, url_for

app = Flask(__name__)


# 1. 自定义响应对象
@app.route('/')
def index():
    # return 'index'  # str/bytes都可以作为视图函数的返回值, 都会被包装成response响应对象

    # 创建响应对象  可以自定义响应头信息
    response = make_response("index")  # type: Response
    print(response.content_type)
    print(response.headers)  # 类字典对象
    return response


# 2. 返回json数据
@app.route('/demo1')
def demo1():
    # json 是一种数据交换格式    js对象 <-->  json字符串  <-->  python类型
    # json中可以存放 字符串/数字, 包含集合有 [] {}
    dict1 = {"name": "zs"}
    # dumps: 归档  dict -> json 字符串
    # json_str = json.dumps(dict1)
    # print(json_str)
    # print(type(json_str))

    # loads:  json字符串 -> dict
    # json_dict = json.loads(json_str)
    # print(json_dict)
    # print(type(json_dict))

    # 直接使用jsonify函数来封装json数据  优点:自动设置content-type为application/json
    # return jsonify(dict1)
    return jsonify(name="zs", age=20)  # 关键字实参形式也可以 数据只能是系统类型


# 3. 重定向
@app.route('/demo2')
def demo2():
    # 可以获取视图函数的URL
    demo1_url = url_for("demo1")
    # return redirect("/demo1")
    return redirect(demo1_url)

    # 重定向, 让前端定向到指定的URL
    # return redirect("http://www.itcast.cn")  # 也会封装为响应对象


# 4. 自定义状态码  方便前端快速排错
@app.route('/demo3')
def demo3():

    return "demo3", 700


if __name__ == '__main__':
    app.run(debug=True)
