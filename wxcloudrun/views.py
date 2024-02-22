from run import app
from flask import request, json
import cryptocode


@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return '欢迎回来！'


@app.route('/api/encrypt', methods=['POST'])
def api_encrypt():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': None}
    # 判断传入的json数据是否为空
    if len(request.get_data()) == 0:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    miyao = request.json.get('miyao')
    message = request.json.get('message')
    miwen = cryptocode.encrypt(message, miyao)

    if len(miwen) != 0:
        return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': miwen}
    print(miwen)
    return return_dict


@app.route('/api/decrypt', methods=['POST'])
def api_decrypt():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': None}
    # 判断传入的json数据是否为空
    if len(request.get_data()) == 0:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    miyao = request.json.get('miyao')
    message = request.json.get('message')
    miwen = cryptocode.decrypt(message, miyao)

    if len(miwen) != 0:
        return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': miwen}
    print(miwen)
    return return_dict
