from django.http import HttpResponse
from django.shortcuts import render
from . import models
# Create your views here.

#добавили код сюда

def hello_world(request):
    return HttpResponse("Hello World!!!")

def post_all(request):
    post = models.Post.objects.all()
    return render(request, "post_list.html", {"post" : post})