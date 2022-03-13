from django.db import models

# Create your models here.

#ls1
class Product(models.Model):
    title = models.CharField(max_length=100)
    weight = models.FloatField()
    price = models.PositiveIntegerField()
    is_stock = models.BooleanField(default=True)
    valid_until = models.DateField()

    def __str__(self):
        return self.title