from django.shortcuts import render

# Create your views here.

#добавил нужные импорты и прописал код для view
from django.http import HttpResponse
from . import models

#hw2
from django.http import Http404
from django.shortcuts import get_object_or_404

#def hello_world(request):
#    return HttpResponse("Hello World!!!")

def book_all(request):
    book = models.Book_shop.objects.all()
    return render(request, "book_list.html", {"book" : book})

#hw2
def get_book_show_detail(request, id):
    try:
        book_show = get_object_or_404(models.Book_shop, id=id)
        try:
            book_comment = models.BookFeedback.objects.filter(book_comment_id=id).\
                order_by("created_date")
        except models.Book_shop.DoesNotExist:
            print("No comments")
    except models.Book_shop.DoesNotExist:
        raise Http404("Book does not exist, try another id")
    return render(request, 'book_detail.html', {"book_show" : book_show, "book_comment" : book_comment })