from django.db import models

# Create your models here.

#написали код тут
class Post(models.Model):
    title = models.CharField(max_length=100) #заголовок поста
    description = models.TextField() #описание поста
    image = models.ImageField(upload_to='') #размещение изображений
    created_date = models.DateField(auto_now_add=True) #дата создания поста
    update_date = models.DateField(auto_now=True) #дата изменения поста
