from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from utils.set_datetime import make_cotation

# Create your views here.
    
    
def home(request):
    return render(request, 'home/pages/home.html', context={
        'dolar': [make_cotation() for _ in range(1)],
    })


def cotacao_sete(request, id):
    return render(request, 'home/pages/dolar_sete_dias.html', context={
        'dolarSete': [make_cotation() for _ in range(7)],

    })


def cotacao_catorze(request, id):
    return render(request, 'home/pages/dolar_catorze_dias.html', context={
        'dolarQuatorze': [make_cotation() for _ in range(14)],

    })
    
def cotacao_vinteum(request, id = 21):
    return render(request, 'home/pages/dolar_vinteum_dias.html', context={
        'dolarVinte': [make_cotation() for _ in range(21)],

    })
    

