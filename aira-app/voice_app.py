# -*- Coding: UTF-8 -*-
#coding: utf-8
#!/usr/bin/env python3

from os import path

if not path.exists("model"):
    print("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit(1)

import json
from tts_utils import *
from asr_utils import *
from data_utils import *
from fake_aira_data import *
from connection import *
from set_interval import *
from random import randrange

@setInterval(10)
def start_send_data(connection, channel):
    if connection.is_open:
        data = json.dumps(fake_aira_data[randrange(99)], indent=4)
        channel.basic_publish(
            exchange='', routing_key='info_from_airaapp', body=data)
        print('AiraApp: Informações de Navegação Enviadas para o Servidor')

postos_combustiveis = load_postos_combustiveis()

def callback_postos_atualizados(ch, method, properties, body):
    print("Received updated event %r" % body)
    if body == b'postos_combustiveis':
        load_postos_combustiveis_data()
        global postos_combustiveis
        postos_combustiveis = load_postos_combustiveis()
        say("Olá Dejair, recebemos uma atualização dos postos de combustíveis")
    if body == b'risco_acidente':
        say("Olá Dejair, detectei um risco de acidente baseado nas informações coletadas até o momento. Não seria um bom momento para fazer uma pausa e descansar um pouquinho?")

def start():
    connection, channel = connect_bus()
    channel.basic_consume(queue='updated', auto_ack=True, on_message_callback=callback_postos_atualizados)
    mq_receive_thread = threading.Thread(target=channel.start_consuming)
    mq_receive_thread.start()

    p, stream, rec = connect_asr()
    send_data_thread = start_send_data(connection, channel)

    while True:
        try:
            # Reconecta no bus se houver perda de conectividade
            if not connection.is_open:
                connection, channel = connect_bus()
                channel.basic_consume(queue='updated', auto_ack=True, on_message_callback=callback)
                mq_receive_thread = threading.Thread(target=channel.start_consuming)
                mq_receive_thread.start()

            # Obtém o stream de audio
            data = stream.read(4000, exception_on_overflow=False)
            if len(data) == 0:
                break

            # Verifica se a voz foi reconhecida
            if rec.AcceptWaveform(data):
                text = json.loads(rec.Result())["text"]
                print(text)

                # Se contém a palavra aira, inicia a comunicação com o motorista
                if "aira" in text:
                    say("Bom dia Dejair")

                # Se perguntou sobre posto mais perto, acessa as informações dos postos
                if "posto" in text and "perto" in text:
                    if postos_combustiveis.empty:
                        say("Desculpe, ainda não tenho nenhum posto na sua localização")
                    else:
                        posto_combustivel = postos_combustiveis.iloc[1]['posto']
                        say("O " + posto_combustivel +
                            " fica a 3 quilômetros da sua posição")
        except:
            channel.stop_consuming()
            connection.close()
            stream.stop_stream()
            stream.close()
            p.terminate()


if __name__ == "__main__":
    start()
