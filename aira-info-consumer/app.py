# -*- Coding: UTF-8 -*-
#coding: utf-8
#!/usr/bin/env python3

import json
import threading
from connection import *
from joblib import load

connection, channel = connect_bus()

classifier = load('naive_bayes.joblib')

def callback_info_from_airaapp(ch, method, properties, body):
    data = json.loads(body)
    data = [[float(data['hipertenso']),
             float(data['diabetico']),
             float(data['km_rodado_dia']),
             float(data['media_horas_sono']),
             float(data['media_agua_diaria']),
             float(data['cigarros_fumados']),
             float(data['horas_descanso']),
             float(data['ansiedade_detectada']),
             float(data['latitude']),
             float(data['longitude'])]]

    result = classifier.predict(data).tolist()[0]
    print(result)
    print(type(result))
    if result == int(1):
        channel.basic_publish(exchange='', routing_key='updated', body="risco_acidente")
        exit(0)

def start():
    try:
        channel.basic_consume(queue='info_from_airaapp', auto_ack=True, on_message_callback=callback_info_from_airaapp)
        mq_receive_thread = threading.Thread(target=channel.start_consuming)
        mq_receive_thread.start()

        while True:
            continue
    except:
        channel.stop_consuming()
        connection.close()

if __name__ == "__main__":
    start()
