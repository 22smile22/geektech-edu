from django.contrib import admin

# Register your models here.

#hw1
from movie_app.models import Director, Movie, Review

admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Review)
