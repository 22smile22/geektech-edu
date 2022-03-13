#hw1
from rest_framework import serializers
from movie_app.models import Director, Movie, Review

class DirectorMovieAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()

class MovieMovieAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewMovieAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
