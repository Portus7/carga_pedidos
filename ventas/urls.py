from django.urls import path
from . import views

urlpatterns = [
    path('get_sales_data/', views.get_sales_data, name='get_sales_data'),
    path('home/', views.index),
    path('carga/', views.carga, name='carga'),
]