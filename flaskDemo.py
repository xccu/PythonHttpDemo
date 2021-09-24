# 需要安装：
#   flask     2.0.1

from flask import Flask, request, jsonify

app = Flask(__name__)

# http://localhost:8080/test?a=1&b=2
@app.route('/test', methods=["GET"])
def calculateGet():
    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    c = int(a) + int(b)
    res = {"result": c}
    return jsonify(content_type='application/json;charset=utf-8',
                   reason='success',
                   charset='utf-8',
                   status='200',
                   content=res)

# http://127.0.0.1:8080/test
@app.route('/test', methods=["POST"])
def calculatePost():
    params = request.form if request.form else request.json
    print(params)
    a = params.get("a", 0)
    b = params.get("b", 0)
    c = a + b
    res = {"result": c}
    return jsonify(content_type='application/json;charset=utf-8',
                   reason='success',
                   charset='utf-8',
                   status='200',
                   content=res)



if __name__ == '__main__':
    app.run(host='0.0.0.0',
            threaded=True,
            debug=False,
            port=8080)

