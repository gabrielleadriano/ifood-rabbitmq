from flask import Flask
from flask_restx import Api


from src.server.pedidos import Pedido

class Consumer():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='1.0',
            title='Consulta',
            description='Consulta',
            doc='/docs'
        )
    
    def run(self, ):
        self.app.run(
            port=8090,
            debug=True
        )

consumer_cliente = Consumer()