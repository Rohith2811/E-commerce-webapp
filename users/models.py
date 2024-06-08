from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE )
    phone_number = models.CharField(max_length=10)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    landmark = models.CharField(max_length=200, blank= True, null=True)
    pincode = models.CharField(max_length=6)
    state = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.username