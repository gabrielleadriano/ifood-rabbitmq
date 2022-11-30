class Pedidos:
    def __init__(self):
        self.lista_pedidos = []

    def adiciona_pedido(self, pedido):
        self.lista_pedidos.append(pedido)

    def retorna_pedido(self, id):
        return next((item for item in self.lista_pedidos if item["id"] == id), None)

    def atualiza_status_pedido(self, pedidoAtualizado):
        pedido = next((item for item in self.lista_pedidos if item["id"] == pedidoAtualizado["id"]), None)
        pedido["status"] = pedidoAtualizado["status"]


