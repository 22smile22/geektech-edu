#hw6
from . import parser_elc, parser_visa, models
from django import forms

class ParserForm(forms.Form):
    MEDIA_CHOICE = (
        ('ELCARD', 'ELCARD'),
        ('VISA', 'VISA'),
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        fields = [
            'media_type',
        ]

    def parse_data(self):
        if self.data['media_type'] == 'ELCARD':
            card_parser = parser_elc.parser_func_elc()
            for e in card_parser:
                models.PaymentCard.objects.create(**e)
        elif self.data['media_type'] == 'VISA':
            card_parser = parser_visa.parser_func_visa()
            for v in card_parser:
                models.PaymentCard.objects.create(**v)
        else:
            pass
