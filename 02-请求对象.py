from flask import Flask,request
from werkzeug.datastructures import FileStorage

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])  # 必须以路径分隔符 / 开头，默认是 get
def index():
    """
    get 解析
    postman—测试url：127.0.0.1:5000/?name=zs&age=18
    运行结果：
    ==============================
    url: http://127.0.0.1:5000/?name=zs&age=18
    method: GET
    headers:
        User-Agent: PostmanRuntime/7.23.0
        Accept: */*
        Cache-Control: no-cache
        Postman-Token: 32080752-cf9d-4655-be91-0d5fd6e03b5b
        Host: 127.0.0.1:5000
        Accept-Encoding: gzip, deflate, br
        Connection: keep-alive
    host: 127.0.0.1:5000
    host 127.0.0.1:5000
    ==============================
    name:zs age:18
    :return:
    """
    # print('='*30)
    # print("url:",request.url)
    # print("method:",request.method)
    # print("headers:\n",request.headers)
    # print("host:",request.headers['Host'])   # 类字典
    # print("host",request.headers.get('Host'))
    # print("="*30)
    #
    # # 获取get的查询字符串  类字典
    # name = request.args.get('name')
    # age = request.args.get('age')
    # print('name:%s age:%s'%(name,age))


    """
    解析 post
    参数：
        x-www-form-urlencoded: 键值对数据  form-post的默认形式
        form-data:  键值对数据&多个文件
        raw: 纯文本内容
        binary:  二进制文件(只能发单个文件)
    """

    """
    url：127.0.0.1:5000/
    """
    # 获取 post 的键值对数据  类字典对象
    username = request.form.get("username")
    print(username)

    # 获取 form-data 形式上传的文件
    avatar_file = request.files.get("avatar")  # type: FileStorage
    # 文件保存早当前路径
    avatar_file.save("avatar.jpg")  # 将文件保存到磁盘中
    print(avatar_file.content_type)  # 获取文件的格式

    # 获取raw(纯文本)和binary(单个二进制文件)形式的数据
    data = request.data
    print(data)  # bytes类型  类str对象  内部包含的是二进制数据
    print(type(data))

    # 编码:文本转为二进制   str.encode() -> bytes
    # 解码:二进制数据转为文本   bytes.decode() -> str
    print(data.decode("utf-8"))

    # wb/rb 对bytes类型数据进行处理
    with open("123.jpg", "wb") as f:
        f.write(data)

    return 'hello post'






if __name__ == '__main__':
    # 保存了该应用页面所有的 路由规则
    print('=====================')
    app.run(host='0.0.0.0', port=5000, debug=False)
