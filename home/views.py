from django.shortcuts import render

# Home view

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

# About Us view
# def about(request):
#    """ A view to return the about us page """
#
#    return render(request, 'about/about.html')