from django.shortcuts import render


def contact_view(request, *args, **kwargs):
    """ Contact page. """
    return render(request, "contact.html", {})
