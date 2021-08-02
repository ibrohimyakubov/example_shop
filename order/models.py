from django.db import models
from basic.models import Product
from user.models import Profile


class ShopCart(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        return self.product.price

    @property
    def count(self):
        return self.quantity * self.product.price


class Order(models.Model):
    STATUS = [
        ('New', 'New'),
        ('Preparing', 'Preparing'),
        ('OnShipping', 'Onshipping'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=10, editable=False)
    total = models.FloatField()
    status = models.CharField(max_length=50, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user.username
