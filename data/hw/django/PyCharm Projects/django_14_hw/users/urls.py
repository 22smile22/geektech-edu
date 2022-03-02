#hw7

from django.urls import path
from . import views

urlpatterns = (
    [
    path('users/', views.UserListView.as_view(), name="user_list"),
    path('register/', views.RegisterView.as_view(), name="registration"),
    path('login/', views.NewLoginView.as_view(), name="login"),
    ]
)