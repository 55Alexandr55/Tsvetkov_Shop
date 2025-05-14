from django.urls import path
from . import views
from .views import create_order

app_name = 'orders'

urlpatterns = [
    path('create/', views.create_order, name='create_order')
]
