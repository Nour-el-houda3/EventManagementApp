from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import login_user
urlpatterns=[
    path('login/',login_user,name="login"),
    path('logout/',LogoutView.as_view(),name="logout")

 ]
