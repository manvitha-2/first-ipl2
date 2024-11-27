from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h2>Kohli is the captain of RCB</h2>')
def vicecaptain(request):
    return HttpResponse('<h2>Plessis is the vicecaptain of RCB</h2>')