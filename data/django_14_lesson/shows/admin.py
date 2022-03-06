from django.contrib import admin

# Register your models here.

#ls2
from . import models

admin.site.register(models.TVShow)
admin.site.register(models.ShowComment)

#ls8
admin.site.register(models.Tag)
admin.site.register(models.Product)
