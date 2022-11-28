import pika, json

connection = pika.BlockingConnection(pika.ConnectionParameters( 'localhost' ))
channel = connection.channel()
channel.queue_declare(queue= 'pedidos-status')

class EnviaPedidoStatus():
    def enviar(pedido):
        pedido_json = json.dumps(pedido)
        channel.basic_publish(exchange='',
                        routing_key='pedidos-status',
                        body=pedido_json) 