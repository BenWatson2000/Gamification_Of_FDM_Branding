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
    stream_type = models.CharField(max_length=50)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class Score(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['player_username', 'game_type'], name='unique_player_game')
        ]
        # unique_together = (('player_username', 'game_type'),)

    player_username = models.CharField(max_length=50)
    game_type = models.CharField(max_length=50, blank=True)
    score = models.IntegerField(blank=True)

    def __str__(self):
        return self.player_username, self.game_type
