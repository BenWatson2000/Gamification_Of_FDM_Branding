from django.db import models
from django.forms import ModelForm


# Create your models here.
class HelperAccount(models.Model):
    # this is just a mock so it will use the auto created id as PK
    username = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(max_length=40, unique=False)
    surname = models.CharField(max_length=40, unique=False)
    password = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username


class GameQuestion(models.Model):
    stream_type = models.CharField(max_length=200)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class Score(models.Model):
    class Meta:
        unique_together = (('username', 'game_type'),)

    username = models.CharField(max_length=50, unique=False)
    game_type = models.CharField(max_length=50, unique=False)
    score = models.CharField(max_length=10, unique=False)

    def __str__(self):
        return self.username, self.game_type
