from celery import shared_task
import lzstring
import json
import redis

# Conexión a Redis
r = redis.Redis(host='localhost', port=6379, db=0)

@shared_task
def save_sales_data(data):
    # Convertir a JSON
    data_json = json.dumps(data)
    # Comprimir con lzstring
    compressed_data = lzstring.LZString().compressToUTF16(data_json)
    # Guardar en Redis
    r.set('cuentas', compressed_data)
    
def get_sales_data_task():
    # Obtener el dato comprimido desde Redis
    compressed_data = r.get('cuentas')
    # Descomprimir con lzstring
    data_json = lzstring.LZString().decompressFromUTF16(compressed_data)
    # Convertir a diccionario de Python
    data = json.loads(data_json)
    return data

@shared_task
def save_orders_clients(orders):
    # Descomprimir con lzstring
    decompressed_orders = lzstring.LZString().decompressFromUTF16(orders)

    # Convertir de JSON a diccionario de Python
    orders_dict = json.loads(decompressed_orders)

    # Guardar los datos en la base de datos
    # for cliente_id, pedidos in orders_dict.items():
    #     for pedido in pedidos:
    #         # Crear y guardar el objeto Orders
    #         order = Orders(pedido_numero=pedido['pedido_numero'], ...)
    #         order.save()

    #         # Crear y guardar los objetos OrdersDetail
    #         for detalle in pedido['detalles']:
    #             order_detail = OrdersDetail(orderobj=order, ...)
    #             order_detail.save()