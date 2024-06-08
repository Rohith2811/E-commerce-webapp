from django.db import models
from django.contrib.auth.models import User
from home.models import Product 

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart_products = models.ManyToManyField(Product, through= 'CartProduct')

    def __str__(self) -> str:
        return f"Cart of {self.user.username}"
    
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} of {self.product.name} in cart of {self.cart.user.username}"