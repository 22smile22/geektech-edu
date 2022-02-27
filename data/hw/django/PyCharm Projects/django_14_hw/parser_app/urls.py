#hw6
from django.urls import path
from . import views

app_name = 'parser'
urlpatterns = [
    path('parser/', views.ParserFormView.as_view(), name='parser'),
    path('card/', views.CardListView.as_view(), name='card_list'),
    path('card/<int:id>/', views.CardDetailView.as_view(), name='card_detail'),
]