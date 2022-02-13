from django.urls import path

#добавил import и urlpattern
from . import views

urlpatterns = [
    path('books/', views.book_all, name='book_list'),
    #path('hello/', views.hello_world, name='hello_world'),
    path("books/<int:id>/", views.get_book_show_detail, name="book_detail") #hw2
]
#