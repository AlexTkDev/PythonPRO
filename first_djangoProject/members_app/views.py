from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest


def index(request):
    return render(request, "index.html")


def input_information(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input')
        if user_input:
            request.session['user_input'] = user_input
            return redirect("show_information")
        else:
            return HttpResponseBadRequest("Invalid input!")
    else:
        return render(request, "input.html")


def show_information(request):
    if request.method == "GET":
        context = {"user_input": request.session.get("user_input")}
        return render(request, "show.html", context)
    else:
        return HttpResponseBadRequest("Invalid request method!")



