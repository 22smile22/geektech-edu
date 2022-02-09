from django.urls import path

#добавил import и urlpattern
from . import views

urlpatterns = [
    path('books/', views.book_all, name='book_list'),
    #path('hello/', views.hello_world, name='hello_world'),
]
#