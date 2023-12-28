from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('login', login),
    path('register', register),
    path("logout", logout_user),
    path("account", account),
    # path("home", home)
]
