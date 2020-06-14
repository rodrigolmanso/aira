from joblib import load, dump
import flask
from flask import request
from flask_cors import CORS, cross_origin
import pandas as pd
from os import path
import pika

app = flask.Flask(__name__)
CORS(app)

def connect_bus():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', heartbeat=6))
    channel = connection.channel()
    channel.queue_declare(queue='updated')
    
    return channel

column_names = ['posto', 'latitude', 'longitude', 'recomendado']
def generate_postos_combustiveis_data():
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

@app.route('/notificar-atualizacao-postos-combustiveis', methods=['POST', 'OPTIONS'])
@cross_origin(origin='*', headers=['Content-Type'])
def notificar_postos_combustiveis_atualizados():
    channel = connect_bus()
    channel.basic_publish(exchange='', routing_key='updated', body="postos_combustiveis")
    return "", 200

@app.route('/notificar-risco-acidente', methods=['POST', 'OPTIONS'])
@cross_origin(origin='*', headers=['Content-Type'])
def notificar_risco_acidente():
    channel = connect_bus()
    channel.basic_publish(exchange='', routing_key='updated', body="risco_acidente")
    return "", 200

if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=True)
