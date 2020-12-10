from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dic = {'insert_me': "Views.py"}
    return render(request, 'cable_app/index.html', context=my_dic)
