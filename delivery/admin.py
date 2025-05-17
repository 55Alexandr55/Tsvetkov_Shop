from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'email', 'delivery_method',
                    'city_description', 'warehouse_description', 'total_price', 'created_at')
    list_filter = ('delivery_method', 'created_at')
    search_fields = ('full_name', 'phone_number', 'email')

