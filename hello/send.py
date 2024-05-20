#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# create a queue
channel.queue_declare(queue="hello")

