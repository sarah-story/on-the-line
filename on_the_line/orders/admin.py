from django.contrib import admin
from .models import Order
from .models import Complete

# Register your models here.
admin.site.register(Order)
admin.site.register(Complete)
