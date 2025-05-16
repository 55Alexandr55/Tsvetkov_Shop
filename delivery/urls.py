from django.urls import path
from . import views

app_name = 'delivery'


urlpatterns = [
    path('', views.delivery_form, name='form'),
    path('api/np/cities/', views.get_np_cities, name='np_cities'),
    path('api/np/warehouses/', views.get_np_warehouses, name='np_warehouses'),
    path('api/np/create-ttn/', views.create_ttn, name='create_ttn'),
    path('api/np/track-ttn/', views.track_ttn, name='track_ttn'),
]
