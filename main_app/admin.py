from django.contrib import admin

# Register your models here.
from .models import Car, Servicing

admin.site.register(Car)
admin.site.register(Servicing)