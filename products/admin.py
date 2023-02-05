from django.contrib import admin
from products import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'brand',
        'description',
        'img_url',
        'rating',
        'price',
        'actual_price',
        'discount',
        'color',
    ]
