from django.shortcuts import render


def todo_view(request, *args, **kwargs):
    """ Todo page. """
    return render(request, "todo.html", {})
