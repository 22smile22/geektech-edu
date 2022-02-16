#ls3
from django import forms
from . import models

class TVShowForm(forms.ModelForm):
    class Meta:
        model = models.TVShow
        fields = "__all__"
        #[
        #     'title'f,
        #     'description'
        # ]
