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
    r.set('sales_data', compressed_data)

@shared_task
def save_orders_clients(orders):
    # Descomprimir con lzstring
    decompressed_orders = lzstring.LZString().decompressFromUTF16(orders)

    # Convertir de JSON a diccionario de Python
    orders_dict = json.loads(decompressed_orders)

    #Aqui procederiamos a guardar los datos necesario en la db