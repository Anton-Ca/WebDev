from django.shortcuts import render


def coming_soon_view(request, *args, **kwargs):
    """ Coming soon... """
    return render(request, "coming-soon.html", {})
