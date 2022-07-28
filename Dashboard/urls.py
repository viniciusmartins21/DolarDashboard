from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    # <int:id> faz com que só seja aceito numeros inteiros com ID da view
    path('detail/<int:id>/', views.details),
]
