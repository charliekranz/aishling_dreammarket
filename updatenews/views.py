from django.shortcuts import render

# Updates and Comments view

def updatenews(request):
    """ A view to return the updates and comments page """

    return render(request, 'updatenews/updatenews.html')
