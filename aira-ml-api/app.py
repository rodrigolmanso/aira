import flask
from flask import request
from flask_cors import CORS, cross_origin
from joblib import load

app = flask.Flask(__name__)
CORS(app)

classifier = load('/app/naive_bayes.joblib')


@app.route('/', methods=['POST','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type'])
def get():
    # Passar payload no seguinte formato
    # {"data":[[1.0, 1.0, 54.0, 6.0, 0.0, 3.0, 6.0, 0, -2.239, 128.37134]]}
    # {"hipertenso": "1", "diabetico": "1", "km_rodado_dia": 54, "media_horas_sono": 6, "media_agua_diaria": 0, "cigarros_fumados": 3, "horas_descanso": 6, "ansiedade_detectada": "0", "latitude": "-2.239", "longitude": "128.37134"}
    data = request.get_json()['data']
    response = {}
    response['classifier'] = classifier.predict(data).tolist()
    return flask.jsonify(response)

if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=True)
