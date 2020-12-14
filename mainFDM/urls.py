from django.urls import path
from . import views

# adding routes to different webpages of this web app
urlpatterns = [
    path('base/', views.base, name='mainFDM-base'),
    path('index/', views.index, name='mainFDM-index'),
    path('', views.home, name='mainFDM-home'),
    path('admin_home/', views.admin_home, name='mainFDM-adminHome'),
    path('admin_home/login/', views.admin_login, name='mainFDM-adminLogin'),
    path('quiz/', views.quiz, name='mainFDM-quiz'),  # route to the page with the pre-stream quiz
]
