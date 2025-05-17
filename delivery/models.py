from django.db import models
import uuid
from django.db import models

class Order(models.Model):
    id_delivery = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    delivery_method = models.CharField(max_length=20, choices=[
        ('pickup', 'Самовывоз'),
        ('np', 'Новая Почта'),
    ])
    city = models.CharField(max_length=255, blank=True, null=True)
    warehouse = models.CharField(max_length=255, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
