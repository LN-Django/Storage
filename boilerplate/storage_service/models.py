from django.db import models
from django.db.models import Min


class Product(models.Model):
    location = models.CharField(max_length=32)
    amount = models.IntegerField(Min(1))
    delivery_time = models.IntegerField(Min(1))
    product_id = models.IntegerField()
