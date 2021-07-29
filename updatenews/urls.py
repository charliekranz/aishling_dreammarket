from . import views
from django.urls import path


urlpatterns = [
    path('about/about.html', views.PostList.as_view(), name='updatenews'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
