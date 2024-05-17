from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from .models import Member


def index(request):
    return render(request, "index.html")


def input_information(request):
    if request.method == "POST":
        if "user_input" in request.POST and request.POST["user_input"]:
            Member.objects.create(save_text=request.POST["user_input"])
            return redirect("show_information")
    return render(request, "input.html")


def show_information(request):
    if request.method == "GET":
        context = {"user_input": Member.objects.all().order_by("-id")}
        return render(request, "show.html", context)
    return HttpResponseBadRequest("Invalid request method!")


def remove_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    member.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
