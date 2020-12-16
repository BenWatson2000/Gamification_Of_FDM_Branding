from django.shortcuts import render
from mainFDM.models import GameQuestion
from random import choices
from django.http import HttpResponse
# Create your views here.

#TODO get 4 random questions and answers with them being "UNIQUE"!

def index(request):

    question_list = GameQuestion.objects.filter()

    questions_for_game = choices(question_list,k=9)

    context = {
        'question_1': questions_for_game[0].question,
        'question_2': questions_for_game[1].question,
        'question_3': questions_for_game[2].question,
        'question_4': questions_for_game[3].question,
        'answer_1': questions_for_game[0].answer,
        'answer_2': questions_for_game[1].answer,
        'answer_3': questions_for_game[2].answer,
        'answer_4': questions_for_game[3].answer
    }

    return render(request, 'cable_app/index.html',context)



