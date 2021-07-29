from django.db import models
from django.contrib.auth.models import User

def updatenews(request):
    context = {
        'posts': posts,
        'title': posts['title']
    }
    return render(request, 'about/about.html', context)
