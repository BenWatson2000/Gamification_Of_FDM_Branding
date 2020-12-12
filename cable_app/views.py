from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


arrayQnA = ''


def index(request):

    return render(request, 'cable_app/index.html',
                  {'content1': arrayQnA})



