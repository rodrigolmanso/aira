# -*- Coding: UTF-8 -*-
#coding: utf-8
#!/usr/bin/env python3

import os

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

import json
from tts_utils import *
from asr_utils import *
from fake_box_data import *
from connection import *
from set_interval import *

@setInterval(10)
def start_send_data(connection, channel):
    if connection.is_open:
        data = json.dumps(fake_box_data[1], indent=4)
        channel.basic_publish(exchange='', routing_key='info_from_boxapp', body=data)
        print('BoxApp: Informações de Navegação Enviadas para o Servidor')
    else:
        print('start_send_data no connection')

def start():
    connection, channel, mq_receive_thread = connect_bus()
    p, stream, rec = connect_asr()
    send_data_thread = start_send_data(connection, channel)

    while True:
        try:
            if not connection.is_open:
                print('BoxApp: Sem conexão com o servidor')
                connection, channel, mq_receive_thread = connect_bus()

            data = stream.read(4000, exception_on_overflow = False)
            if len(data) == 0:
                break

            if rec.AcceptWaveform(data):
                text = json.loads(rec.Result())["text"]

                if "box" in text:
                    channel.basic_publish(exchange='', routing_key='conversation_from_boxapp', body="Dejair: " + text)
                    reply = "Bom dia Dejair"
                    channel.basic_publish(exchange='', routing_key='conversation_from_boxapp', body="BinoBox: " + reply)
                    say(reply)

                if "posto" in text and "perto" in text:
                    channel.basic_publish(exchange='', routing_key='conversation_from_boxapp', body="Dejair: " + text)
                    reply = "Tem um posto de combustível em 3 quilômetros"
                    channel.basic_publish(exchange='', routing_key='conversation_from_boxapp', body="BinoBox: " + reply)
                    say(reply)
        except:
            channel.stop_consuming()
            connection.close()
            stream.stop_stream()
            stream.close()
            p.terminate()

if __name__ == "__main__":
    start()
