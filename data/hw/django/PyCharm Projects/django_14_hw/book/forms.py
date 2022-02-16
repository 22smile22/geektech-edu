#hw3
from django import forms
from . import models

class BookShowForm(forms.ModelForm):
    class Meta:
        model = models.Book_shop
        fields = "__all__"