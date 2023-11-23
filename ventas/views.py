from django.shortcuts import render
from django.http import JsonResponse
import lzstring
from .tasks import r

def get_sales_data(request):
    # Obtener datos de Redis
    compressed_data = r.get('sales_data')

    # Descomprimir con lzstring
    data = lzstring.LZString().decompressFromUTF16(compressed_data)

    return JsonResponse(data, safe=False)