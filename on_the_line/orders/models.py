from django.db import models

# Create your models here.
class Order(models.Model):
    items = models.TextField()
    order_time = models.DateTimeField()
