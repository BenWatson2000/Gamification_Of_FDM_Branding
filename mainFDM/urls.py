from django.urls import path
from . import views

urlpatterns = [
    path('', views.introTGP, name='mainFDM-introTGP'),
    path('quiz/', views.quiz, name='mainFDM-quiz'),
]