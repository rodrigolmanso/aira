# -*- Coding: UTF-8 -*-
#coding: utf-8
#!/usr/bin/env python3

import pika

def connect_bus():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', heartbeat=600))
    channel = connection.channel()
    channel.queue_declare(queue='info_from_airaapp')
    channel.queue_declare(queue='updated')

    return connection, channel
