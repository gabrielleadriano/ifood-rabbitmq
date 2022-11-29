from flask import Flask
from flask_restx import Api

class ServerCliente():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='1.0',
            title='Pedido',
            description='Pedido',
            doc='/docs'
        )
        
    def run(self, ):
        self.app.run(
            port=8085,
            debug=True
        )

server_cliente = ServerCliente()