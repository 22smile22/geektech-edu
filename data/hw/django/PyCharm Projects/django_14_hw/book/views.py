from django.shortcuts import render

# Create your views here.

#добавил нужные импорты и прописал код для view
from django.http import HttpResponse
from . import models

#def hello_world(request):
#    return HttpResponse("Hello World!!!")

def book_all(request):
    book = models.Book_shop.objects.all()
    return render(request, "book_list.html", {"book" : book})