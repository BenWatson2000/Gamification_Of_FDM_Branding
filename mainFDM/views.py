from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.db.models import Max
from .models import GameQuestion, Score
from .forms import AddQuestion, CreateHelperForm, AddScores
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse


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

            # check whether user wants to stay logged in or not
            if request.POST.get('remember-me', None):
                request.session.set_expiry(60 * 60 * 24 * 30)  # keep them logged in for a month
            else:
                request.session.set_expiry(0)  # log them out when the browser closes

            # get data from form
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

    # the question form functionality
    if request.method == "POST":
        q_form = AddQuestion(request.POST)
        if q_form.is_valid():
            question = GameQuestion()
            question.stream_type = q_form.cleaned_data.get("stream_type")
            question.question = q_form.cleaned_data.get("question")
            question.answer = q_form.cleaned_data.get("answer")
            question.save()

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
    # set the game type to the one the user played
    game_played = 'Cable'
    # set the score to the one the user got
    score_got = 734
    # send data to ajax
    data = {}

    # the score adding form functionality
    if request.method == "POST":
        form = AddScores(request.POST)
        if form.is_valid():
            print("form is valid")
            score = Score()
            # get the username
            score.player_username = request.POST.get('player_username')
            # manually set the game type and score to be added to the table as the fields are disabled
            score.game_type = game_played
            score.score = score_got
            try:
                score.save()

                # leaderboard query set
                leaderboard_set = Score.objects.filter(game_type=game_played).order_by('score')[:10]
                leaderboard_set_list = list(leaderboard_set.values())

                data['result'] = 'Submitted'
                data['message'] = 'Your score has been uploaded!'
                data['leaderboard'] = leaderboard_set_list

                return JsonResponse(data, safe=False)

            except IntegrityError as e:
                print("we've got an integrity error")
                data['result'] = 'Integrity Error'
                data['message'] = 'It seems someone with this username has already played this game. ' \
                                  'Choose a different one to save your score!'
                return JsonResponse(data)
        else:
            print('not valid')
            if KeyError:
                print("we've got a key error")
                data['result'] = 'Key Error'
                data['message'] = 'It seems someone with this username has already played this game. ' \
                                  'Choose a different one to save your score!'
                return JsonResponse(data)
            else:
                print('some other errors')
                data['result'] = 'Other Errors'
                data['message'] = 'Something went wrong, please try again.'
                return JsonResponse(data)
    else:
        form = AddScores(initial={'game_type': game_played,
                                  'score': score_got})  # initial={'game_type': game_played, 'score': score_got}

        # pass stuff to the page on load
        context = {
            'form': form,
        }
        return render(request, 'mainFDM/results.html', context)
