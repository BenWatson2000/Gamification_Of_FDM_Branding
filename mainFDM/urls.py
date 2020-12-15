from django.urls import path
from . import views

# adding routes to different webpages of this web app
urlpatterns = [
    path('base/', views.base, name='mainFDM-base'),
    path('index/', views.index, name='mainFDM-index'),
    path('', views.home, name='mainFDM-home'),
    path('helper/home/', views.helper_home, name='mainFDM-helperHome'),
    path('test/login/', views.helper_login, name='mainFDM-helperLogin'),
    path('quiz/', views.quiz, name='mainFDM-quiz'),  # route to the page with the pre-stream quiz
]
