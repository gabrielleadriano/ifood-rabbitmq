import pika
import json
import requests


class Consumer():
    def __init__(self, ):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='pedidos-status')

        def callback(ch, method, properties, body):
            pedido = json.loads(body)

            # envia para o servidor REST
            url = "http://localhost:5000/pedido-status"
            requests.post(url, json=pedido)

        channel.basic_consume(queue='pedidos-status',
                              on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
        connection.close()

    def run(self, ):
        self.app.run(
            debug=True
        )


consumer_cliente = Consumer()
