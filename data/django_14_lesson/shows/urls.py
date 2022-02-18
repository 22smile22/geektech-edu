#ls2
from django.urls import path
from . import views

#ls3
app_name = "shows"

urlpatterns = [
    path("shows/", views.get_shows_all, name="shows_list"),
    path("shows/<int:id>/", views.get_show_detail, name="shows_detail"),
    #ls4
    path("shows/<int:id>/update/", views.put_shows_update, name="shows_update"),
    path("shows/<int:id>/delete/", views.shows_delete, name="shows_delete"),
    #ls3
    path("add-shows/", views.add_show, name="add_show"),
]
