import flask
from flask import request
from flask_cors import CORS, cross_origin
from joblib import load

app = flask.Flask(__name__)
CORS(app)

classifierNAIVE_BAYES = load('naive_bayes.joblib')

@app.route('/', methods=['GET','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type'])
def get():
    data = request.get_json()['data']
    data = [0 if value is None else value for value in data]

    response = {}
    response['classifierNAIVE_BAYES'] = classifierNAIVE_BAYES.predict(data).tolist()
    return flask.jsonify(response)

if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=True)
