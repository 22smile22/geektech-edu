from django.shortcuts import render

# Create your views here.

#hw1
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import \
    DirectorMovieAppSerializer, MovieMovieAppSerializer, ReviewMovieAppSerializer, \
    MoviesReviews
from movie_app.models import Director, Movie, Review
from rest_framework import status

@api_view(['GET'])
def director_list(request):
    directors = Director.objects.all()
    serializer = DirectorMovieAppSerializer(directors, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def director_one(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director Not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorMovieAppSerializer(director)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieMovieAppSerializer(movies, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_one(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie Not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = MovieMovieAppSerializer(movie)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewMovieAppSerializer(reviews, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_one(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review Not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewMovieAppSerializer(review)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_rating_view(request):
    movie = Movie.objects.all()
    serializer = MoviesReviews(movie, many=False)
    return Response(data=serializer.data)