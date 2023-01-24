from django.shortcuts import render


def jess_view(request, *args, **kwargs):
    """ Jess page. """
    return render(request, "jess.html", {})
