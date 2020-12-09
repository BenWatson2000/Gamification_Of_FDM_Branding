from django.shortcuts import render
from django.http import HttpResponse
from .models import AdminAccounts


# Create your views here.

# view of the intro to FDM Technical Graduate Programmes page
def index(request):
    return render(request, 'mainFDM/index.html')


def base(response):
    return render(response, 'mainFDM/base.html')


def home(response):
    return render(response, 'mainFDM/home.html', {})


def admin_home(response, id):
    user = AdminAccounts.objects.get(id=id)
    return render(response, 'mainFDM/admin_home.html', {"user":user})


def stream_select(request):
    # using the django.shortcut render to add templates
    return render(request, 'mainFDM/stream_select.html', {})  # passing information into our intro_tgp template


# view of the pre-stream quiz page
def quiz(request):
    return render(request, 'mainFDM/quiz.html', {})  # passing info to the quiz.html template
