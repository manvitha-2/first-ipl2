from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h2>Hardik is the captain of mi</h2>')
def vicecaptain(request):
    return HttpResponse('<h2>Bumrah is the vicecaptain of mi</h2>')