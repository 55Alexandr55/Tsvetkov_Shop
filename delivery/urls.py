from django.urls import path
from . import views

app_name = 'delivery'


urlpatterns = [
    path('api/get_cities/', views.get_np_cities, name='get_np_cities'),
    path('api/get_warehouses/', views.get_np_warehouses, name='get_np_warehouses'),
    path('', views.delivery_form, name='delivery_form'),
]
