import json
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import GameQuestion, Score
from .forms import AddQuestion, CreateHelperForm, AddScores
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse
import cable_app.views as c
import memoryApp.views as m
import pipeGameApp.views as p


# Create your views here.

# view of the intro to FDM Technical Graduate Programmes page
def index(request):
    return render(request, 'mainFDM/index.html')


def base(response):
    return render(response, 'mainFDM/base.html')


def home(request):
    # update the results page boolean check
    request.session["played"] = False
    if request.method == "POST":

        request.session["stream-type"] = request.POST.get("stream-type-holder")

        game_type = request.POST.get("game-type-holder")
        request.session["my_game"] = game_type

        if game_type == 'Cable':
            return redirect(c.index)
        elif game_type == "Pipe":
            return redirect(p.index)
        elif game_type == "Memory":
            return redirect(m.index)

    return render(request, 'mainFDM/home.html')


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

            # verify the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # check if the user has been approved by the admin
                if user.helper.admin_approved:
                    login(request, user)
                    return redirect('helperHome')
                # not approved yet
                else:
                    messages.info(request, 'Your account has not yet been approved by the admins.\nThis may take up to '
                                           '24h.')
            else:
                messages.error(request, 'Please enter a correct username and password.\nNote that both fields '
                                        'may be case-sensitive.')

        context = {'form': form}
        # using the django.shortcut render to add templates
        return render(request, 'mainFDM/helper_login.html', context)  # passing information into our intro_tgp template


def helper_logout(request):
    logout(request)
    return redirect('helperLogin')


@login_required
def helper_home(request):
    # data to be passed to the template
    context = {}

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
    context['q_form'] = q_form

    # the best score functionality
    best_cable = Score.objects.filter(game_type='Cable').order_by('score')[:1]
    best_memo = Score.objects.filter(game_type='Memory').order_by('score')[:1]
    best_pipes = Score.objects.filter(game_type='Pipes').order_by('score')[:1]

    for ca in best_cable:
        context['best_cable'] = ca
    for me in best_memo:
        context['best_memo'] = me
    for pi in best_pipes:
        context['best_pipes'] = pi

    # display the list of questions already in the database
    # query the database
    qs = GameQuestion.objects.all()
    # create a list of values from the queryset to prepare for passing to template
    qs_list = list(qs.values())

    # previous methods, don't delete yet
    # context['questions'] = qs
    # context['qscount'] = range(1, qs.count()+1)

    # pass the list as json to template
    context['qsjson'] = json.dumps(qs_list)

    return render(request, 'mainFDM/helper_home.html', context)


# view of the pre-stream quiz page
def quiz(request):
    return render(request, 'mainFDM/quiz.html', {})  # passing info to the quiz.html template


# view of the results page
def results(request):
    # check if the key exists yet - in case someone opens results page from url before opening home page
    # if they key does not exist, create it as False (not played yet) and throw them to the home page
    if "played" not in request.session:
        request.session["played"] = False
        return redirect(home)

    # if this user has not yet played
    if request.session["played"] is None or not request.session["played"]:
        return redirect(home)

    else:  # if they have played - display the results page for them

        # set the game type to the one the user played
        game_played = request.session["my_game"]
        # set the score to the one the user got
        score_got = request.session["my_score"]
        # get the stream type the user entered
        stream_type = request.session["stream-type"]

        # send data to ajax
        data = {'game': game_played}

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
                                      'score': score_got})

            # change the shortcuts to real stream names before passing it to the page
            if stream_type == 'BI':
                stream_type = 'Business Intelligence'
            elif stream_type == 'ST':
                stream_type = 'Software Testing'
            else:
                stream_type = 'Technical Operations'

            # pass stuff to the page on load
            context = {
                'form': form,
                'stream_type': stream_type,
                'game': game_played,
                'tweetURL': 'https://twitter.com/intent/tweet?'
                            'text=I%20just%20got%20a%20time%20of%20' + score_got + '%20on%20the%20' + game_played + ' Game%21%20Try'
                                                                                                                    '%20and%20beat%20my%20time%20at%20https%3A//mycareerpath.co.uk%20and%20di'
                                                                                                                    'scover%20many%20different%20career%20sectors%20in%20technology%21&hashtags=MYCAREERPATH',
            }
            return render(request, 'mainFDM/results.html', context)
