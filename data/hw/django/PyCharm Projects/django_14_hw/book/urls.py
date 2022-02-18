from django.urls import path

#добавил import и urlpattern
from . import views

app_name = "book_shows" #hw3

urlpatterns = [
    path('books/', views.book_all, name='book_list'),
    #path('hello/', views.hello_world, name='hello_world'),
    path("books/<int:id>/", views.get_book_show_detail, name="book_detail"), #hw2
    path("add-books/", views.add_book, name = "add_books"), #hw3
    path("books/<int:id>/update/", views.put_book_update, name = "book_update"), #hw4
    path("books/<int:id>/delete/", views.book_delete, name = "book_delete"), #hw4
]
#