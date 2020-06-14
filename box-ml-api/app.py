import flask
from flask import request
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
CORS(app)

@app.route('/', methods=['GET','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type'])
def get():
    data = request.get_json()
    #flask.jsonify(data)
    return data, 200

if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=True)
