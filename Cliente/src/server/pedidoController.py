from flask_restx import Resource
import pika
import json

from src.server.server import server_cliente

connection = pika.BlockingConnection(pika.ConnectionParameters( 'localhost' ))
channel = connection.channel()
channel.queue_declare(queue= 'pedidos')

app, api = server_cliente.app, server_cliente.api

@api.route('/pedido')
class RecebePedido(Resource):
    def post(self, ):
        response = api.payload
        pedido = json.dumps(response)
        envia_pedido(pedido)
        return response, 200
    
def envia_pedido(pedido):
    channel.basic_publish(exchange='',
                      routing_key='pedidos',
                      body=pedido) 
    print("Pedido enviado")