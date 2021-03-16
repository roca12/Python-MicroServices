#amqps://kremiiqx:YzeK4jz5VYpCbpxr16ePDlkqiH5QSEeE@gull.rmq.cloudamqp.com/kremiiqx
import pika

params = pika.URLParameters("amqps://kremiiqx:YzeK4jz5VYpCbpxr16ePDlkqiH5QSEeE@gull.rmq.cloudamqp.com/kremiiqx")

connection=pika.BlockingConnection(params)

channel= connection.channel()

def publish():
    channel.basic_publish(exchange='',routing_key='main',body='hello main')