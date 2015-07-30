from django.db import models

# Create your models here.
class Order(models.Model):
    items = models.TextField()
    order_time = models.DateTimeField()
    order_id = models.CharField(max_length = 100, null=True)
    phone = models.CharField(max_length = 20, null=True)

class Complete(models.Model):
    items = models.TextField()
    order_time = models.DateTimeField()
    order_id = models.CharField(max_length = 100, null=True)
    phone = models.CharField(max_length = 11, null=True)
