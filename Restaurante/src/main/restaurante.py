import json
import time
from enum import Enum
from src.controllers.pedidoStatusController import *

global lista_pedidos
lista_pedidos = []

# enum com status possiveis para o pedido
class PedidoStatus(Enum):
    PROCESSAMENTO = 1
    PRODUCAO = 2
    ENTREGA = 3
    FINALIZADO = 4

class Restaurante:
    # altera status do pedido atual
    def altera_status(pedido):
        if pedido["status"] == PedidoStatus.PROCESSAMENTO.value:
            time.sleep(5)
            pedido["status"] = PedidoStatus.PRODUCAO.value
        elif pedido["status"] == PedidoStatus.PRODUCAO.value:
            time.sleep(5)
            pedido["status"] = PedidoStatus.ENTREGA.value 
        elif pedido["status"] == PedidoStatus.ENTREGA.value:
            time.sleep(10)
            pedido["status"] = PedidoStatus.FINALIZADO.value 

    # recebe o pedido e inicia o processamento pelo status
    def recebe_pedido(self, pedido):
        pedido_dict = json.loads(pedido)
        lista_pedidos.append(pedido_dict.copy())
        self.processa_pedidos(self)

    # processa todos os pedidos, alterando os status
    # quando finaliza remove o pedido da lista
    def processa_pedidos(self):
        while len(lista_pedidos) > 0:
            for i in range(len(lista_pedidos)):
                self.altera_status(lista_pedidos[i])
                print("enviando status")
                EnviaPedidoStatus.enviar(lista_pedidos[i])
                if lista_pedidos[i]["status"] == PedidoStatus.FINALIZADO.value:
                    lista_pedidos.remove(lista_pedidos[i])
            


         