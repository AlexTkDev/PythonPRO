from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "messenger_app/base.html")
