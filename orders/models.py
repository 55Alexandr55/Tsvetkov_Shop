from django.db import models

class Order(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    city_ref = models.CharField(max_length=50)
    warehouse_ref = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ttn = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Замовлення від {self.full_name}"