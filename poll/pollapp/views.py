from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    template = "pollapp/index.html"
    return render(request, template, context=None)


def contact_view(request):
    template = "pollapp/contact.html"
    return render(request, template, context=None)


