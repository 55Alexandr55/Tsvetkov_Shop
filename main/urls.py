from django.urls import path
from .views import CatalogView, ItemDetailView, item_search, item_autocomplete

from . import views

app_name = 'main'

urlpatterns = [
    path('', CatalogView.as_view(), name='catalog'),  
    path('item/<slug:slug>/', ItemDetailView.as_view(), name='item_detail'),
    path('search/', item_search, name='item_search'),
    path('autocomplete/', item_autocomplete, name='item_autocomplete'),

]