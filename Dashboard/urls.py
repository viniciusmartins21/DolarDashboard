from unicodedata import name
from django.urls import path

from . import views

    # <int:id> faz com que só seja aceito numeros inteiros com ID da view
    # <int:slug> faz com que só seja aceito strings ligadas com (-) exemplo ( /cotacao/dolar-sete-dias/ ) 
urlpatterns = [
    path('', views.home, name="home-dolar"),
    
    path('cotacao_sete/<int:id>/', views.cotacao_sete, name='dolar-sete-dias'),
    path('cotacao_catorze/<int:id>/', views.cotacao_catorze,name="dolar-14-dias"),
    path('cotacao_vinteum/<int:id>/', views.cotacao_vinteum,name="dolar-21-dias"),
    
]
