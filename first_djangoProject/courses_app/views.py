from django.shortcuts import render

# Create your views here.


def is_auntification(request):
    return render(request, "auntification_information.html")