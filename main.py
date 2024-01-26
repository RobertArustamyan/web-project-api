# app.py
from flask import Flask, request, jsonify
from getting_json_req import MakingJson

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')

    json_obj = MakingJson()
    json_obj.start(value=query)
    result = json_obj.making_body()

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
