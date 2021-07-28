from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('updatenews.html', views.updatenews, name='updatenews'),
#    path('', views.PostList.as_view(), name='home'),
#    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
