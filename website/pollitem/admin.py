from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'sku', 'stock', 'price')
    ordering = ('category',)

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)