# Create your views here.

#ls2
from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404
from django.http import Http404

#ls3
from . import forms #ls3
from django.http import HttpResponse
from django.shortcuts import reverse, redirect

#ls5
from django.views import generic

class ShowsListView(generic.ListView):
    template_name = "shows_list.html"
    queryset = models.TVShow.objects.all()

    def get_queryset(self):
        return self.queryset

# def get_shows_all(request):
#     shows = models.TVShow.objects.all()
#     # shows = models.TVShow.objects.filter(genre='Drama') #ls3
#     # shows = models.TVShow.objects.order_by("-id") #ls3
#     return render(request, "shows_list.html", {"shows" : shows})

class ShowsDetailView(generic.DetailView):
    template_name = "shows_detail.html"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.TVShow, id=shows_id)

# def get_show_detail(request, id):
#     try:
#         show = get_object_or_404(models.TVShow, id=id)
#         try:
#             comment = models.ShowComment.objects.filter(shows_id=id).order_by("created_date")
#         except models.TVShow.DoesNotExist:
#             print('No comments')
#     except models.TVShow.DoesNotExist:
#         raise Http404('TVSHOW does not exist, try another id')
#     return render(request, "shows_detail.html", {"show": show, 'shows_comment': comment})

class ShowsCreateView(generic.CreateView):
    template_name = "add_shows.html"
    form_class = forms.TVShowForm
    queryset = models.TVShow.objects.all()
    success_url = "/shows/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ShowsCreateView, self).form_valid(form=form)


# #ls3
# def add_show(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.TVShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("shows:shows_list"))
#             # return HttpResponse("Show Created Successfully")
#     else:
#         form = forms.TVShowForm()
#     return render(request, "add_shows.html", {"form" : form})

class ShowsUpdateView(generic.UpdateView):
    template_name = "shows_update.html"
    form_class = forms.TVShowForm
    success_url = "/shows/"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.TVShow, id=shows_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ShowsUpdateView, self).form_valid(form=form)

    # def get_success_url(self):
    #     return redirect(reverse("shows:shows_list"))


# #ls4
# def put_shows_update(request, id):
#     show_id = get_object_or_404(models.TVShow, id=id)
#     if request.method == "POST":
#         form = forms.TVShowForm(instance=show_id,
#                                 data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("shows:shows_list"))
#     else:
#         form = forms.TVShowForm(instance=show_id)
#     return render(request, "shows_update.html", {"form": form,
#                                                  "show": show_id})


class ShowsDeleteView(generic.DeleteView):
    success_url = "/shows/"
    template_name = "confirm_delete_show.html"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.TVShow, id=shows_id)

# def shows_delete(request, id):
#     show_id = get_object_or_404(models.TVShow, id=id)
#     show_id.delete()
#     # return HttpResponse("Show Deleted")
#     return redirect(reverse("shows:shows_list"))


#ls8

class ProductListView(generic.ListView):
    template_name = "product_list.html"
    queryset = models.Product.objects.all()


    def get_queryset(self):
        return self.queryset

