from django.shortcuts import render

# Create your views here.
#hw7

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from . import forms, models

class NewLoginView(LoginView):
    # form_class = AuthenticationForm
    form_class = forms.LoginForm
    success_url = '/users/'
    template_name = "login.html"

class RegisterView(CreateView):
    # form_class = UserCreationForm
    form_class = forms.RegistrationForm
    template_name = 'registration.html'
    success_url = "/users/"

class UserListView(ListView):
    # queryset = User.objects.all()
    queryset = models.CustomUser.objects.all()
    template_name = "user_list.html"

    def get_queryset(self):
        return self.queryset

