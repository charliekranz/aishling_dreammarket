from . import views
from django.urls import path


urlpatterns = [
    path('updatenews.html', views.PostList.as_view(), name='updatenews'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
