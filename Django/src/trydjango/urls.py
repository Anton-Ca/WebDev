"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Own
from homepage.views import home_view
from contact.views import contact_view
from jess.views import jess_view, jess_heart, jess_quiz
from comingSoon.views import coming_soon_view
from todo.views import todo_view
from code_projects.views import chatbot_view

urlpatterns = [
    path("", home_view, name='home'),
    path("home/", home_view, name='home'),
    path("contact/", contact_view, name='contact'),
    path("chatbot/", chatbot_view, name='chatbot'),
    path("jess/", jess_view, name='jess'),
    path("a<3j/", jess_heart, name='anton<3jess'),
    path("A<3J/", jess_heart, name='anton<3jess'),
    path("jess_quiz/", jess_quiz, name='quiz'),
    path("coming-soon/", coming_soon_view, name='coming-soon'),
    path("todo/", todo_view, name='todo'),
    path("admin/", admin.site.urls),
]
