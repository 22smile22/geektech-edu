from django.db import models

# Create your models here.
#hw6

class PaymentCard(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='')

