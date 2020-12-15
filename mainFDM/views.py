from django.shortcuts import render
from django.db.models import Max
from .models import GameQuestion, Score
from .forms import AddQuestion


# Create your views here.

# view of the intro to FDM Technical Graduate Programmes page
def index(request):
    return render(request, 'mainFDM/index.html')


def base(response):
    return render(response, 'mainFDM/base.html')


def home(response):
    return render(response, 'mainFDM/home.html', {})


def helper_home(request):
    # the question form functionality
    if request.method == "POST":
        q_form = AddQuestion(request.POST)
        if q_form.is_valid():
            question = GameQuestion()
            question.stream_type = q_form.cleaned_data.get("stream_type")
            question.question = q_form.cleaned_data.get("question")
            question.answer = q_form.cleaned_data.get("answer")
            question.save()
        else:
            q_form = AddQuestion()

    q_form = AddQuestion()

    # the highest score functionality
    score_dict = Score.objects.filter().aggregate(Max('score'))
    highest_score = score_dict.get('score__max')

    # pass stuff to the page
    context = {
        'q_form': q_form,
        'highest_score': highest_score
    }

    return render(request, 'mainFDM/helper_home.html', context)


def helper_login(request):
    # using the django.shortcut render to add templates
    return render(request, 'mainFDM/helper_login.html', {})  # passing information into our intro_tgp template


# view of the pre-stream quiz page
def quiz(request):
    return render(request, 'mainFDM/quiz.html', {})  # passing info to the quiz.html template
