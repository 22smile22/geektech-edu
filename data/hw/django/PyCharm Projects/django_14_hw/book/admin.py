from django.contrib import admin

# Register your models here.

#добавил импорт и админ сайт
from . import models

admin.site.register(models.Book_shop)