from django.db import models

# Create your models here.

#создание класса book
class Book_shop(models.Model):
    title = models.CharField(max_length=64) # Название книги
    description = models.TextField() # Аннотация книги
    image = models.ImageField(upload_to='') # Изображения в книге
    created_date = models.DateField(auto_now_add=True) # Дата публикации книги
    update_date = models.DateField(auto_now=True) # Дата внесения последних правок
    author = models.CharField(max_length=48) # Автор книги
