#amqps://kremiiqx:YzeK4jz5VYpCbpxr16ePDlkqiH5QSEeE@gull.rmq.cloudamqp.com/kremiiqx
import pika

params = pika.URLParameters(
    "amqps://kremiiqx:YzeK4jz5VYpCbpxr16ePDlkqiH5QSEeE@gull.rmq.cloudamqp.com/kremiiqx")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, propierties, body):
    print('Recibido en admin')
    print(body)

channel.basic_consume(queue='admin',on_message_callback=callback)
print('consumidor iniciado')
channel.start_consuming()
channel.close()