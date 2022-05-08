"""afisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from movie_app import views #hw1
from users import views as user_views #hw5

from django.conf import settings #hw7
from django.conf.urls.static import static  #hw7

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/directors/', views.director_list),
    # path('api/v1/directors/', views.director_list_create_view),
    # path('api/v1/directors/<int:id>/', views.director_one),
    path('api/v1/directors/', views.DirectorListAPIView.as_view()),  #hw6
    path('api/v1/directors/<int:pk>/', views.DirectorItemAPIView.as_view()),  #hw6
    # path('api/v1/movies/', views.movie_list),
    # path('api/v1/movies/', views.movie_list_create_view),
    # path('api/v1/movies/<int:id>/', views.movie_one),
    path('api/v1/movies/', views.MovieListAPIView.as_view()),  #hw6
    path('api/v1/movies/<int:pk>/', views.MovieItemAPIView.as_view()),  #hw6
    # path('api/v1/reviews/', views.review_list),
    # path('api/v1/reviews/', views.review_list_create_view),
    # path('api/v1/reviews/<int:id>/', views.review_one),
    path('api/v1/reviews/', views.ReviewListViewSet.as_view()),  #hw6
    path('api/v1/reviews/<int:pk>/', views.ReviewItemAPIView.as_view()),  #hw6
    path('api/v1/movies/reviews/', views.movie_rating_view),
    # path('api/v1/register/', user_views.registration),  #hw5
    # path('api/v1/login/', user_views.authorization),  #hw5
    path('api/v1/register/', user_views.RegisterAPIView.as_view()),  #hw6
    path('api/v1/login/', user_views.AuthAPIView.as_view()),  #hw6
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  #hw7
