from django.contrib import admin

# Register your models here.
from .models import Category, product
admin.site.register(product)
admin.site.register(Category)
