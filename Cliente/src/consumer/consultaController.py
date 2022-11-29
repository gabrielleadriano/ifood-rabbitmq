from flask_restx import Resource

from src.consumer.consumer import consumer_cliente
from src.server.pedidos import Pedido

app, api = consumer_cliente.app, consumer_cliente.api

@api.route('/pedido/<int:index>')
class BuscaPedido(Resource):
    def get(self, index):
        return Pedido.buscaPedido(index), 200

