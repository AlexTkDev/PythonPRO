from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import UserMessage
from .form import UserLoginForm, UserRegistrationForm


# Create your views here.
def index(request):
    messages = UserMessage.objects.all().order_by('-date_sent')
    context = {
        "messages": messages,
        "title": "Messenger",
    }
    return render(request, "messenger_app/index.html", context)


@login_required
def save_text(request):
    if request.method == "POST":
        message_text = request.POST.get("message_text", "")
        if message_text:
            UserMessage.objects.create(message=message_text, author=request.user)
            return redirect('index')
        else:
            messages = UserMessage.objects.all().order_by('-date_sent')
            context = {
                "messages": messages,
                "error": "Сообщение не может быть пустым.",
                "title": "Messenger"
            }
            return render(request, "messenger_app/index.html", context)
    return redirect('index')


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    context = {"form": form, "title": "Авторизация"}
    return render(request, "messenger_app/login.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {"form": form, "title": "Регистрация"}
    return render(request, "messenger_app/register.html", context)


def logout(request):
    auth.logout(request)
    return redirect('index')
