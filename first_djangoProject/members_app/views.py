from django.shortcuts import render


# Create your views here.
def input_information(request):
    return render(request, "input.html")


def show_information(request):
    return render(request, "show.html")
