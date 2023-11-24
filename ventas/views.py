import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
import lzstring
from .tasks import r, save_sales_data, get_sales_data_task, save_orders_clients


def index(response):
    # Ejecutar tarea en segundo plano
    # Renderizar página HTML con datos de Redis
    # context = {'sales_data': r.get('sales_data')}
    return render(response, 'base.html', {})

def carga(request):
    if request.method == 'POST':
        data_file = request.FILES['dataFile']

        # Leer los datos del archivo
        data = json.load(data_file)

        # Imprimir los datos para depuración
        result = save_sales_data.delay(data)
        data = result.get()
        print(data)
        return render(request, 'base.html')
    return render(request, 'base.html')

def get_sales_data(request):
    # Obtener datos de Redis
    print(get_sales_data_task.delay())
    compressed_data = get_sales_data_task.delay()
    print(compressed_data)
    # Descomprimir con lzstring
    data_json = lzstring.LZString().decompressFromUTF16(compressed_data)

    # Convertir la cadena JSON a un diccionario
    data = json.loads(data_json)

    return JsonResponse(data, safe=False)

def guardar_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        r.set('order_data', json.dumps(data))
        save_orders_clients.delay(json.dumps(data))
        return JsonResponse({'message': 'orden guardada correctamente'})
    else:
        return JsonResponse({'error': 'metodo invalido'})