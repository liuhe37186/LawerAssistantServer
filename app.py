from flask import Flask, jsonify, request, render_template
from flask import abort
from flask import make_response
from user.user import user
from bean.response import ResponseBean

app = Flask(__name__)
app.register_blueprint(user, url_prefix='/user')
versionCode = '11'
res = ResponseBean()
tasks = {
    'code': 1,
    'msg': 'success',
    'data': [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'done': False
        },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web',
            'done': False
        }
    ]
}


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1.0/app/tasks', methods=['GET'])
def get_tasks():
    res.data = "xxxx"
    print(res.data)
    return jsonify(data=res.data, code=res.code, msg=res.msg)


@app.route('/api/v1.0/app/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks['data'] if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/api/v1.0/app/update', methods=['POST', 'GET'])
def check_update():
    data = {'content': '解决已知bug\n优化用户体验', 'url': "http://www.baidu.com", "isForce": "1"}

    if request.method == 'POST':
        code = request.form.get("version_code")
        print(code)
    else:
        code = request.args.get('version_code')
        print(code)
    if code >= versionCode:
        res.data = ""
    else:
        res.data = data
    return jsonify(code=res.code, msg=res.msg,data=data)


if __name__ == '__main__':
    app.run(host='18.220.87.46', port=8989)
