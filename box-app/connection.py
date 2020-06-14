# -*- Coding: UTF-8 -*-
#coding: utf-8
#!/usr/bin/env python3

import pika
import threading
from tts_utils import *

def callback(ch, method, properties, body):
    print("Received updated event %r" % body)
    if body == b'postos_combustiveis':
        say("Olá Dejair, recebemos uma atualização dos postos de combustíveis")

def connect_bus():
    print('connecting to bus...')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='events_from_boxapp')
    channel.queue_declare(queue='updated')
    channel.basic_consume(queue='updated', auto_ack=True, on_message_callback=callback)
    mq_receive_thread = threading.Thread(target=channel.start_consuming)
    mq_receive_thread.start()

    return connection, channel, mq_receive_thread    
