from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
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
    # TODO log users out after they close their session
    # keys = request.session.keys()
    # user = request.session['_auth_user_id']
    # items = request.session.items()
    # print(user)
    # print(items)

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
    submitted = False
    # set the game type to the one the user played
    game_played = 'Cable'
    # set the score to the one the user got
    score_got = 734

    # the question form functionality
    if request.method == "POST":
        form = AddScores(request.POST)
        if form.is_valid():
            print("form is valid")
            score = Score()
            # get the username
            score.player_username = form.cleaned_data.get("player_username")
            # manually set the game type and score to be added to the table as the fields are disabled
            score.game_type = game_played
            score.score = score_got
            try:
                score.save()
                messages.info(request, 'Your score has been uploaded!')
                print('message sent')
                # TODO find a way to either display a different thing on form submission or change the form submit
                #  button to 'show leaderboard'
                submitted = True
                return redirect('results')
                # this allows for displaying different content on the page after submission but is not the best way
                # return render(request, 'mainFDM/results.html', {"submitted": submitted})
            except IntegrityError as e:
                print("we've got an integrity error")
                messages.info(request, 'It seems someone with this username has already played this game. '
                                       'Choose a different one to save your score!')
        else:
            print('not valid')
            if KeyError:
                print("we've got a key error")
                messages.info(request, 'It seems someone with this username has already played this game. '
                                       'Choose a different one to save your score!')
            else:
                print('some other errors')
                messages.info(request, 'Something went wrong, please try again.')

    form = AddScores(initial={'game_type': game_played,
                              'score': score_got})  # initial={'game_type': game_played, 'score': score_got}
    print(submitted)
    # pass stuff to the page
    context = {
        'form': form,
        'submitted': submitted,
    }
    return render(request, 'mainFDM/results.html', context)
