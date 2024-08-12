from django.contrib import admin
from produtos.models import Brands, Products

@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Products)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('sku', 'title', 'price', 'brand')