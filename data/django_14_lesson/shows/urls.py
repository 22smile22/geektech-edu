#ls2
from django.urls import path
from . import views

#ls5
from . import models

#ls3
app_name = "shows"

urlpatterns = [
    # path("shows/", views.get_shows_all, name="shows_list"),
    path("shows/", views.ShowsListView.as_view(),
         name="shows_list"), #ls5
    path("shows/anime/", views.ShowsListView.as_view(queryset=models.TVShow.objects.filter(genre="Anime")
                                                     .order_by("-id")),name="shows_anime_list"),
    path("shows/action/", views.ShowsListView.as_view(queryset=models.TVShow.objects.filter(genre="Action")
                                                     .order_by("-id")), name="shows_action_list"),
    path("shows/drama/", views.ShowsListView.as_view(queryset=models.TVShow.objects.filter(genre="Drama")
                                                     .order_by("-id")), name="shows_drama_list"),

    # path("shows/<int:id>/", views.get_show_detail, name="shows_detail"),
    path("shows/<int:id>/", views.ShowsDetailView.as_view(),
         name="shows_detail"), #ls5
    #ls4
    # path("shows/<int:id>/update/", views.put_shows_update, name="shows_update"),
    path("shows/<int:id>/update/", views.ShowsUpdateView.as_view(), name="shows_update"),
    # path("shows/<int:id>/delete/", views.shows_delete,name="shows_delete"),
    path("shows/<int:id>/delete/", views.ShowsDeleteView.as_view(),name="shows_delete"),
    #ls3
    # path("add-shows/", views.add_show,name="add_show"),
    path("add-shows/", views.ShowsCreateView.as_view(), name="add_show"),
]
