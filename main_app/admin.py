from django.contrib import admin

# Register your models here.
from .models import Car, Servicing, Mod

admin.site.register(Car)
admin.site.register(Servicing)
admin.site.register(Mod)
