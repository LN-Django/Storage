from django.db import models

from .validators import validate_higher_or_equals_one


class Product(models.Model):
    location = models.CharField(max_length=32)
    amount = models.IntegerField(validators=[validate_higher_or_equals_one])
    delivery_time = models.IntegerField(
        validators=[validate_higher_or_equals_one])
    product_id = models.IntegerField()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Product, self).save(*args, **kwargs)

class CompleteProduct(Product):
    name = models.CharField(max_length=64)
    base_price = models.IntegerField()
    description = models.CharField(max_length=128)
    weight = models.FloatField()
    category = models.CharField(max_length=32)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(CompleteProduct, self).save(*args, **kwargs)
