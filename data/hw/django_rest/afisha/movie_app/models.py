from django.db import models

# Create your models here.

#hw1
class Director(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        return self.movies.all().count()

class Movie(models.Model):
    title = models.CharField(max_length=90)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    # director = models.ForeignKey(Director, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, related_name='movies',
                                 null=True)

    def __str__(self):
        return self.title

#hw2
    # @property
    # def filtered_reviews(self):
    #     return self.reviews.filter(stars__gte=4)
    #
    # @property
    # def reviews_count(self):
    #     # return self.reviews.filter(stars__gte=4).count()
    #     return self.filtered_reviews.count()

    @property
    def average_rating(self):
        # return self.reviews.aggregate(models.Avg('stars')).get('stars__avg')
        return self.reviews.aggregate(models.Avg('stars')).get('stars__avg')

CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

class Review(models.Model):
    text = models.TextField()
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True,
                                related_name='reviews')
    stars = models.IntegerField(default=1, choices=CHOICES)


    def __str__(self):
        return self.text