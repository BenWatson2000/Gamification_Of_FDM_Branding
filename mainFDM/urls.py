from django.urls import path
from . import views

# adding routes to different webpages of this web app
urlpatterns = [
    path('base/', views.base, name='mainFDM-base'),
    path('index/', views.index, name='mainFDM-index'),
    path('', views.home, name='home'),
    path('helper/home/', views.helper_home, name='helperHome'),
    path('helper/login/', views.helper_login, name='helperLogin'),
    path('helper/register/', views.helper_register, name='helperRegister'),
    path('helper/logout/', views.helper_logout, name='helperLogout'),
    # path('quiz/', views.quiz, name='quiz'),  # route to the page with the pre-stream quiz
    path('results/', views.results, name='results'),  # route to the page with the pre-stream quiz
]
