from django.db import models

# Create your models here.

#hw1
class Director(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=90)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text