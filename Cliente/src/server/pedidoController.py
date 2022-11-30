import pika, json
from flask_restx import Resource

from src.server.server import server_cliente
from src.main.pedidos import *

connection = pika.BlockingConnection(pika.ConnectionParameters( 'localhost' ))
channel = connection.channel()
channel.queue_declare(queue= 'pedidos')

app, api = server_cliente.app, server_cliente.api
pedidosInstance = Pedidos()


def envia_pedido(pedido):
    channel.basic_publish(exchange='',
                      routing_key='pedidos',
                      body=pedido) 

# comunicacao REST
@api.route('/pedido','/pedido/<int:id>')
class RecebePedido(Resource):
    # retorna o pedido 
    async def get(self, id):
        return await pedidosInstance.retorna_pedido(id)
        

    def post(self, ):
        pedido = api.payload

        pedido["id"] = len(pedidosInstance.lista_pedidos) + 1
        pedido["status"] = 1

        #adiciona pedido à lista de pedidos global
        pedidosInstance.adiciona_pedido(pedido)

        pedidoString = json.dumps(pedido)
        envia_pedido(pedidoString)

        return pedido, 200
    
# atualiza status do pedido
@api.route('/pedido-status')
class PedidoStatus(Resource):
    def post(self, ):
        pedidoAtualizado = api.payload 
        pedidosInstance.atualiza_status_pedido(pedidoAtualizado)
        return "pedido atualizado com sucesso", 200
