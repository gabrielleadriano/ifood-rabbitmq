# import json
# import pika

# global lista_pedidos
# lista_pedidos = {}

# class Pedido:
    
#     def run():
#         connection = pika.BlockingConnection(pika.ConnectionParameters( 'localhost' ))
#         channel = connection.channel()
#         channel.queue_declare(queue='pedidos-status')
        
#         def callback(ch, method, properties, body):
#             print("recebido", body)
#             pedido_dict = json.loads(body)
#             codigo = pedido_dict["codigo"] 
#             lista_pedidos[codigo] = pedido_dict
#             print("Adicionado ",lista_pedidos)
#             channel.stop_consuming()


#         channel.basic_consume(queue='pedidos-status', on_message_callback=callback, auto_ack=True)
#         channel.start_consuming()
        
        
#     def buscaPedido(index):
#         Pedido.run()
#         print(lista_pedidos)
#         return lista_pedidos[index]