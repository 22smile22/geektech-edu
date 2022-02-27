from django.shortcuts import render

# Create your views here.
#hw6

from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, FormView, DetailView
from . import parser_elc, parser_visa, models, forms
from django.http import HttpResponse

class ParserFormView(FormView):
    template_name = "parser.html"
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            # return HttpResponse('Parser Success')
            return redirect(reverse('parser:card_list'))
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)

class CardListView(ListView):
    template_name = 'card.html'
    queryset = models.PaymentCard.objects.all()

    def get_queryset(self):
        return self.queryset


class CardDetailView(DetailView):
    template_name = "card_detail.html"

    def get_object(self, **kwargs):
        card_detail = self.kwargs.get("id")
        return get_object_or_404(models.PaymentCard, id=card_detail)