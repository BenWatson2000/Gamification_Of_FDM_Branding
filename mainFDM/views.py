from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Max
from .models import GameQuestion, Score
from .forms import AddQuestion, CreateHelperForm, AddScores
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.

# view of the intro to FDM Technical Graduate Programmes page
def index(request):
    return render(request, 'mainFDM/index.html')


def base(response):
    return render(response, 'mainFDM/base.html')


def home(response):
    return render(response, 'mainFDM/home.html', {})


def helper_register(request):
    if request.user.is_authenticated:
        return redirect('helperHome')
    else:
        form = CreateHelperForm()

        if request.method == 'POST':
            form = CreateHelperForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, username + ', you have successfully created a helper account!')
                return redirect('helperLogin')

        context = {'form': form}
        return render(request, 'mainFDM/helper_register.html', context)


def helper_login(request):
    if request.user.is_authenticated:
        return redirect('helperHome')
    else:
        form = AuthenticationForm()
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('helperHome')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {'form': form}
        # using the django.shortcut render to add templates
        return render(request, 'mainFDM/helper_login.html', context)  # passing information into our intro_tgp template


def helper_logout(request):
    logout(request)
    return redirect('helperLogin')


@login_required
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


# view of the pre-stream quiz page
def quiz(request):
    return render(request, 'mainFDM/quiz.html', {})  # passing info to the quiz.html template


# view of the pre-stream quiz page
def results(request):
    # # the question form functionality
    # if request.method == "POST":
    #     form = AddScores(request.POST)
    #     if form.is_valid():
    #         question = GameQuestion()
    #         question.stream_type = q_form.cleaned_data.get("stream_type")
    #         question.question = q_form.cleaned_data.get("question")
    #         question.answer = q_form.cleaned_data.get("answer")
    #         question.save()
    #     else:
    #         q_form = AddQuestion()

    form = AddScores(initial={'game_type': 'Memory', 'score': 500})

    # pass stuff to the page
    context = {
        'form': form,

    }
    return render(request, 'mainFDM/results.html', context)

