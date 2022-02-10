from django.urls import path

#добавил импорт и урлпаттерн
from . import views

urlpatterns = [
    path('posts/', views.post_all, name='post_list'),
    path('hello/', views.hello_world, name='hello_world'),
]
#