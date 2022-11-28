from flask import Flask
from flask_restx import Api, Resource
import pika
import json

from src.server.instance import server

connection = pika.BlockingConnection(pika.ConnectionParameters( 'localhost' ))
channel = connection.channel()
channel.queue_declare(queue= 'pedidos')

app, api = server.app, server.api

teste = 'retorno rabbit'

@api.route('/pedido')
class GerenciaPedido(Resource):
    def get(self, ):
        return teste
    
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
    # connection.close()