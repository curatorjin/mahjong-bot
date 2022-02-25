from flask import Flask, request, jsonify
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/', methods=['POST'])
@cross_origin()
def log_info():
    with open('../info.txt', 'ab+') as f:
        f.write(request.data)
        f.write(b"\n")
        f.flush()
    print(request.data)
    return ""


if __name__ == '__main__':
    app.run('0.0.0.0', 12121, ssl_context='adhoc')
