from django.conf import settings
from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __def__(self):
        return self.name

class OrderItem(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __def__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateField(auto_now_add=True)
    ordered_date = models.DateField()
    orderd = models.BooleanField(default=False)

    def __def__(self):
        return self.user.username
