#hw1
from rest_framework import serializers
from movie_app.models import Director, Movie, Review

class ReviewMovieAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = '__all__'
        fields = 'id text stars'.split()


class DirectorMovieAppSerializer(serializers.ModelSerializer):
    # movie = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movies_count'.split()

class MovieMovieAppSerializer(serializers.ModelSerializer):
    director = DirectorMovieAppSerializer()
    reviews = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        # fields = '__all__'
        fields = 'id title director reviews reviews_count average_rating'.split()

    def get_reviews(self, movie):
        filtered_reviews = movie.reviews.filter(stars__gte=4)
        return ReviewMovieAppSerializer(filtered_reviews, many=True).data

    def get_reviews_count(self, movie):
        return movie.reviews.filter(stars__gte=4).count()


class MoviesReviews(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title average_rating'.split()

