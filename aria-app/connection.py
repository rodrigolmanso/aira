# -*- Coding: UTF-8 -*-
#coding: utf-8
#!/usr/bin/env python3

import pika
import threading
from tts_utils import *
from data_utils import *

def connect_bus():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600))
    channel = connection.channel()
    channel.queue_declare(queue='info_from_ariaapp')
    channel.queue_declare(queue='updated')

    return connection, channel
