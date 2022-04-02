#hw1
from rest_framework import serializers
from movie_app.models import Director, Movie, Review
#hw4
from rest_framework.exceptions import ValidationError

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
        fields = '__all__'

#hw4
class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=30)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=16)
    description = serializers.CharField(min_length=2, max_length=77)
    duration = serializers.IntegerField()
    director_id = serializers.IntegerField()


    def validate(self, attrs):
        try:
            Director.objects.get(id=attrs['director_id'])
        except Director.DoesNotExist:
            raise ValidationError(f'Director with id {attrs["director_id"]} does not exist')
        return attrs


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=2, max_length=300)
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField()