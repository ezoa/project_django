from django.contrib import admin
from django.db import models
from .models import Product
# Register your models here.

#prepopulate the slug

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','price','stock','category','modified_date','is_availabe')
    prepopulated_fields={'slug':('product_name',)}
    list_display = ('product_name','slug')



admin.site.register(Product,ProductAdmin)
