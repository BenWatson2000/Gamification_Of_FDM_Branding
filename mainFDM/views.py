from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def introTGP(request):
    return HttpResponse('<h1>Main FDM with the intro to Graduate Programmes</h1>')


def quiz(request):
    return HttpResponse('<h1> This is where the pre-stream quiz will open</h1>')