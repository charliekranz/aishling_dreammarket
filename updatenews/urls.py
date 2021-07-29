from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('updatenews.html', views.updatenews, name='updatenews'),
    path('/updatenews/updatenews.html', views.PostList.as_view(), name='updatenews'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
