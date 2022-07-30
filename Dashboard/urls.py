from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home),
    
    # <int:id> faz com que só seja aceito numeros inteiros com ID da view
    # <int:slug> faz com que só seja aceito strings ligadas com (-) exemplo ( /cotacao/dolar-sete-dias/ ) 
    path('cotacao_sete/<slug:id>/', views.cotacao_sete),
    path('cotacao/<slug:id>/', views.cotacao_catorze),
    path('cotacao/<slug:id>/', views.cotacao_vinte_um),
    
]
