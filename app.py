import flask
from flask_cors import CORS
from searchEngine import SearchEngineBase, Collection_data

app = flask.Flask(__name__)
CORS(app)


@app.route('/search', methods=['GET', 'POST'])
def search():
    # 从参数当中获取搜索内容
    query = flask.request.args.get('query')
    # 搜索
    result = search_engine.search(query)
    if result == set():
        result = 'No result'
        response = {
            'code': -1,
            'msg': result,
        }
        return flask.jsonify(response)
    else:
        result = list(result)
        # 将日期类型转化为字符串
        # 将id类型转化为字符串
        for t in result:
            t['date'] = t['date'].strftime('%Y-%m-%d')
            t['_id'] = str(t['_id'])
        response = {
            'code': 200,
            'msg': result,
        }
        return flask.jsonify(response)


@app.route('/index', methods=['GET'])
def index():
    # 获取页面
    return flask.render_template('index.html')


if __name__ == '__main__':
    search_engine = SearchEngineBase()
    search_engine.data = Collection_data
    search_engine.split_words()
    search_engine.create_index()
    app.run(host='0.0.0.0', port=5000, debug=True)
