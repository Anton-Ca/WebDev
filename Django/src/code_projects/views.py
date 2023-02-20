from django.shortcuts import render

def chatbot_view(request, *args, **kwargs):
    """ Chatbot page. """
    return render(request, "chatbot.html", {})
