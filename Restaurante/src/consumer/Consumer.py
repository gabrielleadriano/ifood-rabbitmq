import pika
from src.controllers.restaurante import *

class Consumer():
    def __init__(self, ):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='pedidos')

        def callback(ch, method, properties, body):
            # print(" [x] Recebido %r" % body)
            print(Restaurante.recebe_pedido(Restaurante, body))

        channel.basic_consume(queue='pedidos', on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
        connection.close()
    
    def run(self, ):
        self.app.run(
            debug=True
        )

consumer = Consumer()