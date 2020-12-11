from django.shortcuts import render
from django.http import HttpResponse
from .models import GameQuestion, Score
from .forms import AddQuestion, HighestScore


# Create your views here.

# view of the intro to FDM Technical Graduate Programmes page
def index(request):
    return render(request, 'mainFDM/index.html')


def base(response):
    return render(response, 'mainFDM/base.html')


def home(response):
    return render(response, 'mainFDM/home.html', {})


def admin_home(request):
    # the question form functionality
    if request.method == "POST":
        q_form = AddQuestion(request.POST)
        s_form = HighestScore(request.POST)
        if q_form.is_valid():
            question = GameQuestion()
            question.stream_type = q_form.cleaned_data.get("stream_type")
            question.question = q_form.cleaned_data.get("question")
            question.answer = q_form.cleaned_data.get("answer")
            question.save()
        else:
            q_form = AddQuestion()
            s_form = HighestScore()

    q_form = AddQuestion()
    s_form = HighestScore()

    # pass stuff to the page
    context = {
        'q_form': q_form,
        's_form': s_form,
    }

    return render(request, 'mainFDM/admin_home.html', context)


def stream_select(request):
    # using the django.shortcut render to add templates
    return render(request, 'mainFDM/stream_select.html', {})  # passing information into our intro_tgp template


# view of the pre-stream quiz page
def quiz(request):
    return render(request, 'mainFDM/quiz.html', {})  # passing info to the quiz.html template
