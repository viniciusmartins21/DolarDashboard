from django.urls import path
from Dashboard.views import home  

urlpatterns = [
    path('', home),
]