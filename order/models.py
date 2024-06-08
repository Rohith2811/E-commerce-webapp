from django.db import models
from django.utils import timezone
from home.models import Product
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products_ordered = models.ManyToManyField(Product, through='OrderedProduct')   
    def __str__(self) -> str:
        return f"Orders of {self.user.username}"

class OrderedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.quantity} of {self.product.name} ordered by {self.order.user.username}"