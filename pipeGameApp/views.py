from django.shortcuts import render
from mainFDM.models import GameQuestion
from random import choices
from django.http import HttpResponse
# Create your views here.

def index(request):

    question_list = GameQuestion.objects.filter()

    mockArray = [None]*4
    questions_for_game= [None]*4
    counter =0

    # making sure that every question is unique
    while counter<4:
        choice = choices(question_list, k=1)
        if counter==0:
            mockArray[0]=choice[0].question
            questions_for_game[0] = choice[0]
            counter+=1
        elif counter==1:
            if mockArray[0]!= choice[0].question:
                mockArray[1] = choice[0].question
                questions_for_game[1] = choice[0]
                counter += 1
        elif counter==2:
            if mockArray[0]!= choice[0].question and mockArray[1]!= choice[0].question:
                mockArray[2] = choice[0].question
                questions_for_game[2] = choice[0]
                counter += 1
        elif counter==3:
            if mockArray[0]!= choice[0].question and mockArray[1]!= choice[0].question and mockArray[2]!= choice[0].question:
                mockArray[3] = choice[0].question
                questions_for_game[3] = choice[0]
                counter += 1


    context = {
        'question_1': questions_for_game[0].question,

        'answer_1': questions_for_game[0].answer,
        'answer_2': questions_for_game[1].answer,
        'answer_3': questions_for_game[2].answer

    }

    return render(request, 'pipeGameApp/index.html',context)

