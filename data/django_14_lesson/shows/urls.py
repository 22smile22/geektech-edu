#ls2
from django.urls import path
from . import views

#ls3
app_name = "shows"

urlpatterns = [
    path("shows/", views.get_shows_all, name="shows_list"),
    path("shows/<int:id>/", views.get_show_detail, name="shows_detail"),
    #ls3
    path("add-shows/", views.add_show, name="add_shows"),
]
