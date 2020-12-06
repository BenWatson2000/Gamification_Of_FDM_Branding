from django.urls import path
from . import views

# adding routes to different webpages of this web app
urlpatterns = [
    path('', views.home, name='mainFDM-home'),
    path('admin_home/<int:id>', views.admin_home, name='mainFDM-adminHome'),  # route to the intro page to FDM Technical Graduate Programmes
    path('streams/', views.stream_select, name='mainFDM-streamSelect'),
    path('streams/quiz/', views.quiz, name='mainFDM-quiz'),  # route to the page with the pre-stream quiz
]
