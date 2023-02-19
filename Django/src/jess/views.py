from django.shortcuts import render


def jess_view(request, *args, **kwargs):
    """ Jess page. """
    return render(request, "jess.html", {})


def jess_heart(request, *args, **kwargs):
    """ Jess valentines solution/reward page. """
    return render(request, "jess_heart.html", {})


def jess_quiz(request, *args, **kwargs):
    """ Jess valentines quiz page. """
    return render(request, "jess_quiz.html", {})
