from django.contrib import admin

# Register your models here.

#ls1
from products.models import Product

admin.site.register(Product)