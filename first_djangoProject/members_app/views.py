from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .models import Member


def index(request):
    return render(request, "index.html")


def input_information(request):
    if request.method == "POST":
        Member.objects.create(save_text=request.POST["user_input"])
        return redirect("show_information")
    return render(request, "input.html")


def show_information(request):
    if request.method == "GET":
        context = {"user_input": Member.objects.all()}
        return render(request, "show.html", context)
    return HttpResponseBadRequest("Invalid request method!")
