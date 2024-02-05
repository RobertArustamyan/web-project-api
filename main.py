# app.py
from flask import Flask, request, jsonify
from getting_json_req import MakingJson
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')

    json_obj = MakingJson()
    json_obj.start(value=query)
    result = json_obj.making_body()

    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
