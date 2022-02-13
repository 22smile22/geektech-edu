from django.contrib import admin

# Register your models here.

#ls2
from . import models

admin.site.register(models.TVShow)
admin.site.register(models.ShowComment)
