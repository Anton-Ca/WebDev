from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    """ Home page. """
    context = {}
    return render(request, "home.html", context)     #HttpResponse("<h1> Hello World! </h1>")
