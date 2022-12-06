from django.contrib import admin

# Register your models here.
from .models import Products, Sails, Employees, Inventory

admin.site.register(Products)
admin.site.register(Sails)
admin.site.register(Employees)
admin.site.register(Inventory)