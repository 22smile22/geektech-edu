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


def get_shows_all(request):
    shows = models.TVShow.objects.all()
    # shows = models.TVShow.objects.filter(genre='Drama') #ls3
    # shows = models.TVShow.objects.order_by("-id") #ls3
    return render(request, "shows_list.html", {"shows" : shows})

def get_show_detail(request, id):
    try:
        show = get_object_or_404(models.TVShow, id=id)
        try:
            comment = models.ShowComment.objects.filter(shows_id=id).order_by("created_date")
        except models.TVShow.DoesNotExist:
            print('No comments')
    except models.TVShow.DoesNotExist:
        raise Http404('TVSHOW does not exist, try another id')
    return render(request, "shows_detail.html", {"show": show, 'shows_comment': comment})

#ls3
def add_show(request):
    method = request.method
    if method == 'POST':
        form = forms.TVShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("shows:shows_list"))
            # return HttpResponse("Show Created Successfully")
    else:
        form = forms.TVShowForm()
    return render(request, "add_shows.html", {"form" : form})





