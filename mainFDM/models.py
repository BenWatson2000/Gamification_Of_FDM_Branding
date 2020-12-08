from django.db import models

# TODO: Figure out how to change the view of the table to display the column names
# TODO: also, figure out whether this is actually a table xdddd
# Create your models here.
class AdminAccounts(models.Model):
    # this is just a mock so it will use the auto created id as PK
    username = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(max_length=40, unique=False)
    surname = models.CharField(max_length=40, unique=False)
    password = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username

# class GameSession(models.Model):
#     player = models.CharField(max_length=)
