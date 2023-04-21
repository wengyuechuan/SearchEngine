from flask import Flask, jsonify, render_template, request
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app, supports_credentials=True)


@app.route("/", methods=["GET", "POST"])
def first():
    response = {
        "code": 200,
        "msg": "success"
    }
    return jsonify(response)


@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/test", methods=["GET"])
def test():
    # 获取query参数
    name = request.args.get("query")
    return "name"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
