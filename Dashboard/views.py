from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home/pages/home.html')


def cotacao_sete(request, id):
    return render(request, 'home/pages/dolar-sete-dias.html')


def cotacao_catorze(request, id):
    return render(request, 'home/pages/dolar-catorze-dias.html')


def cotacao_vinte_um(request, id):
    return render(request, 'home/pages/dolar-vinte-um-dias.html')


