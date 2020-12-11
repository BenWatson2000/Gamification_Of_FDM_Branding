from django.db import models
from django.forms import ModelForm

# TODO: Figure out how to change the view of the table to display the column names
# TODO: also, figure out whether this is actually a table xdddd

# stream choices
STREAM_TYPES = (
    ("Select", "Select Stream Type"),
    ("TOP", "Technical Operations"),
    ("BI", "Business Intelligence"),
    ("ST", "Software Testing"),
)


# Create your models here.
class AdminAccounts(models.Model):
    # this is just a mock so it will use the auto created id as PK
    username = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(max_length=40, unique=False)
    surname = models.CharField(max_length=40, unique=False)
    password = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username


class GameQuestions(models.Model):
    stream_type = models.CharField(max_length=3, choices=STREAM_TYPES)
    question = models.CharField()
    answer = models.CharField()
    incorrect1 = models.CharField()
    incorrect2 = models.CharField()
    incorrect3 = models.CharField()

    def __str__(self):
        return self.question

class QuestionForm(ModelForm):
    class Meta:
        model: GameQuestions
        fields = ['stream_type', 'question', 'answer', 'incorrect1', 'incorrect2', 'incorrect3']


# class GameSession(models.Model):
#     player = models.CharField(max_length=)