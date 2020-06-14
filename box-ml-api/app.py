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

@app.route('/', methods=['GET','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type'])
def get():
    data = request.get_json()
    #flask.jsonify(data)
    return data, 200

if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=True)
