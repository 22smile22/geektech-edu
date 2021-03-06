from django.shortcuts import render

# Create your views here.

#добавил нужные импорты и прописал код для view
from django.http import HttpResponse
from . import models

#hw2
from django.http import Http404
from django.shortcuts import get_object_or_404

#hw3
from . import forms
from django.http import HttpResponse
from django.shortcuts import reverse, redirect

#hw5
from django.views import generic

#def hello_world(request):
#    return HttpResponse("Hello World!!!")

class BookListView(generic.ListView):
    template_name = "book_list.html"
    queryset = models.Book_shop.objects.all()

    def get_queryset(self):
        return self.queryset

# def book_all(request):
#     book = models.Book_shop.objects.all()
#     return render(request, "book_list.html", {"book" : book})

class BookDetailView(generic.DetailView):
    template_name = "book_detail.html"

    def get_object(self, **kwargs):
        book_show = self.kwargs.get("id")
        return get_object_or_404(models.Book_shop, id=book_show)

# #hw2
# def get_book_show_detail(request, id):
#     try:
#         book_show = get_object_or_404(models.Book_shop, id=id)
#         try:
#             book_comment = models.BookFeedback.objects.filter(book_comment_id=id).\
#                 order_by("created_date")
#         except models.Book_shop.DoesNotExist:
#             print("No comments")
#     except models.Book_shop.DoesNotExist:
#         raise Http404("Book does not exist, try another id")
#     return render(request, 'book_detail.html', {"book_show" : book_show, "book_comment" : book_comment })

class BookCreateView(generic.CreateView):
    template_name = "add_books.html"
    form_class = forms.BookShowForm
    queryset = models.Book_shop.objects.all()
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)

# #hw3
# def add_book(request):
#     method = request.method
#     if method == "POST":
#         form = forms.BookShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("book_shows:book_list"))
#     else:
#         form = forms.BookShowForm()
#     return render(request, "add_books.html", {"form" : form})

class BookUpdateView(generic.UpdateView):
    template_name = "book_update.html"
    form_class = forms.BookShowForm
    success_url = "/books/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book_shop, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookUpdateView, self).form_valid(form=form)

# #hw4
# def put_book_update(request, id):
#     book_id = get_object_or_404(models.Book_shop, id=id)
#     if request.method == "POST":
#         form = forms.BookShowForm(instance=book_id,
#                                   data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("book_shows:book_list"))
#     else:
#         form = forms.BookShowForm(instance=book_id)
#     return render(request, "book_update.html", {"form":form,
#                                                   "book_show":book_id})

class BookDeleteView(generic.DeleteView):
    success_url = "/books/"
    template_name = "book_delete.html"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book_shop, id=book_id)

# def book_delete(request, id):
#     book_id = get_object_or_404(models.Book_shop, id=id)
#     book_id.delete()
#     return redirect(reverse("book_shows:book_list"))