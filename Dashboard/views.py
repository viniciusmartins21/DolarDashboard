from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from utils.set_datetime import make_cotation

    


# Create your views here.
    
    
def home(request):
    return render(request, 'home/pages/home.html', context={
        'dolars': [make_cotation() for _ in range(2)],
    })


def cotacao_sete(request, id):
    return render(request, 'home/pages/dolar-sete-dias.html', context={
        'dolar': [make_cotation() for _ in range(8)],
    })

