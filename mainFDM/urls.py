from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# adding routes to different webpages of this web app
urlpatterns = [
    path('base/', views.base, name='mainFDM-base'),
    path('index/', views.index, name='mainFDM-index'),

    path('', views.home, name='home'),

    path('helper/home/', views.helper_home, name='helperHome'),
    path('helper/login/', views.helper_login, name='helperLogin'),
    path('helper/register/', views.helper_register, name='helperRegister'),
    path('helper/logout/', views.helper_logout, name='helperLogout'),

    # submit email for password reset
    path('helper/reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # email sent success message
    path('helper/reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # link to password reset form from email
    path('helper/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # password successfully changed message
    path('helper/reset_password_completed/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('results/', views.results, name='results'),  # route to the page with the pre-stream quiz
]
