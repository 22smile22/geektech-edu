#hw7

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #, UsernameField
from . import models

class RegistrationForm(UserCreationForm):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_TYPE = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    )
    OCUP_CHOICE = (
        ("STUDENT", "Student"),
        ("WORKER", "Worker"),
        ("JOBLESS", "Jobless"),
        ("RETIRED", "Retired"),
        ("FREELANCE", "Freelance"),
        ("REMOTE", "Remote"),
    )
    EDUCATION = (
        ("BACHELOR", "Bachelor"),
        ("MASTER", "Master"),
        ("ENGINEER", "Engineer"),
    )
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    occupation = forms.ChoiceField(choices=OCUP_CHOICE, required=True)
    secret_pass = forms.CharField(required=True)
    education = forms.ChoiceField(choices=EDUCATION, required=True)

    class Meta:
        model = models.CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "gender",
            "occupation",
            "phone_number",
            "secret_pass",
            "education",
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "email",
                "id": "email"
                }
            )
        )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "type password",
                "id": "password"
            }
        )
    )
