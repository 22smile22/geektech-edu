#ls6
from . import parser, models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOICE = (
        ('ANIME', 'ANIME'),
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        fields = [
            'media_type',
        ]

    def parse_data(self):
        if self.data['media_type'] == 'ANIME':
            anime_parser = parser.parser_func()
            for i in anime_parser:
                models.Film.objects.create(**i)
