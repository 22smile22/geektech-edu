from django.contrib import admin

# Register your models here.

#ls1
from products.models import Product
#ls2
from products.models import Brand, Review

admin.site.register(Brand) #ls2
admin.site.register(Product)
admin.site.register(Review) #ls2
