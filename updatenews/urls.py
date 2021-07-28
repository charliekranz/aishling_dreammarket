from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('updatenews.html', views.updatenews, name='updatenews'),
]
