from joblib import load, dump
import flask
from flask import request
from flask_cors import CORS, cross_origin
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import os.path
from os import path
import pika
import time

app = flask.Flask(__name__)
CORS(app)

while True:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        channel.queue_declare(queue='updated')
        break
    except:
        time.sleep(0.1)


column_names = ['posto', 'latitude', 'longitude', 'recomendado']
def generate_postos_combustiveis_data():
    channel.basic_publish(exchange='', routing_key='updated', body="postos_combustiveis")

    df = pd.DataFrame(columns=column_names)
    rows = [{'posto': 'posto são paulo', 'latitude': 1, 'longitude': 1, 'recomendado': True}, {'posto': 'posto curitiba', 'latitude': 2, 'longitude': 2, 'recomendado': True}, {'posto': 'posto rio de janeiro', 'latitude': 3, 'longitude': 3, 'recomendado': True}, ]
    for row in rows:
        df.loc[len(df)] = row
    dump(df, 'postos_combustiveis.joblib')
    return df

df = load('postos_combustiveis.joblib') if path.exists("postos_combustiveis.joblib") else generate_postos_combustiveis_data()


@app.route('/postos-combustiveis', methods=['GET', 'OPTIONS'])
@cross_origin(origin='*', headers=['Content-Type'])
def get_postos_combustiveis():
    result = flask.jsonify(df.to_dict(orient='records'))
    return result, 200

@app.route('/postos-combustiveis', methods=['POST', 'OPTIONS'])
@cross_origin(origin='*', headers=['Content-Type'])
def post_postos_combustiveis():
    channel.basic_publish(exchange='', routing_key='updated', body="postos_combustiveis")
    return "", 200

if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=True)
