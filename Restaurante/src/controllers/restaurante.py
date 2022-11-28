import json
import time
from enum import Enum

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
            time.sleep(5)
            pedido["status"] = PedidoStatus.FINALIZADO.value 

    # recebe o pedido e inicia o processamento pelo status
    def recebe_pedido(self, pedido):
        pedido_dict = json.loads(pedido)
        lista_pedidos.append(pedido_dict.copy())
        # self.altera_status(lista_pedidos[0])
        self.processa_pedidos()
        return lista_pedidos

    # processa todos os pedidos, alterando os status
    def processa_pedidos(self):
        while len(lista_pedidos) > 0:
            for i in len(lista_pedidos):
                self.altera_status(lista_pedidos[i])
            


         