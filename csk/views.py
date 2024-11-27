from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h2>Ruthuraj is the captain of CSK</h2>')
def vicecaptain(request):
    return HttpResponse('<h2>jadeja is the vicecaptain of CSK</h2>')