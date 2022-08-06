from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from utils.set_datetime import make_cotation

# Create your views here.
    
    
def home(request):
    return render(request, 'home/pages/home.html', context={
        'dolar': [make_cotation() for _ in range(1)],
        'dolarSete': [make_cotation() for _ in range(7)],
        'dolarQuatorze': [make_cotation() for _ in range(14)],
        'dolarVinte': [make_cotation() for _ in range(21)],
    })


# def cotacao_sete(request, id):
#     return render(request, 'home/pages/dolar-sete-dias.html', context={
#         'dolars': [make_cotation() for _ in range(8)],
#     })

