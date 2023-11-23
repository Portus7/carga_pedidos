from django.urls import path
from . import views

urlpatterns = [
    # ... tus otras rutas aquí ...

    path('get_sales_data/', views.get_sales_data, name='get_sales_data'),
]