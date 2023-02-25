from django.shortcuts import render

def chatbot_view(request, *args, **kwargs):
    """ Chatbot page. """
    if request.method == 'POST':
        post_data = request.POST
        print(post_data)

        message = post_data.get('message', '')

    return render(request, "chatbot.html", {})
