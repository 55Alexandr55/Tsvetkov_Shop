from django.db import models
import uuid
from django.db import models
from cart.cart import Cart

class Order(models.Model):
    id_delivery = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    email = models.EmailField()
    full_name = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=13)
    delivery_method = models.CharField(max_length=20, choices=[
        ('pickup', 'Самовывоз'),
        ('np', 'Новая Почта'),
    ])
    city_ref = models.CharField(max_length=50, blank=True, null=True)  # Ref города
    city_description = models.CharField(max_length=255, blank=True, null=True)  # Название города
    warehouse_description = models.CharField(max_length=255, blank=True, null=True)  # Название отделения
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
        return f"Заказ от {self.full_name} ({self.delivery_method})"