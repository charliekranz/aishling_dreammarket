from django.shortcuts import render

# Contact view

def contact(request):
    """ A view to return the about us page """

    return render(request, 'contact/contact.html')
