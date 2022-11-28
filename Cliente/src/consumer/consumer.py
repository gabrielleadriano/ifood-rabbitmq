import pika
from src.main.pedidos import *

class Consumer():
    def __init__(self, ):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='pedidos-status')

        def callback(ch, method, properties, body):
            print("recebido", body)

        channel.basic_consume(queue='pedidos-status', on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
        connection.close()
    
    def run(self, ):
        self.app.run(
            debug=True
        )

consumer_cliente = Consumer()