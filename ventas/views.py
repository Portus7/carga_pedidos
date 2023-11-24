import json
from django.shortcuts import render
from django.http import JsonResponse
import lzstring
from .tasks import r, save_sales_data, get_sales_data_task


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
        print(data)
        save_sales_data(data)
        return render(request, 'base.html')
    return render(request, 'base.html')

def get_sales_data(request):
    # Obtener datos de Redis
    print(get_sales_data_task())
    compressed_data = r.get('ejemplo')
    print(compressed_data)
    # Descomprimir con lzstring
    data_json = lzstring.LZString().decompressFromUTF16(compressed_data)

    # Convertir la cadena JSON a un diccionario
    data = json.loads(data_json)

    return JsonResponse(data, safe=False)