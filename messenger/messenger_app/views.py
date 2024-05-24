from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import UserMessage
from .form import UserLoginForm, UserRegistrationForm


# Create your views here.
@login_required(login_url='login')
def index(request):
    messages = UserMessage.objects.all().order_by('-date_sent')
    for message in messages:
        message.can_delete_by_user = message.can_delete(request.user)
    give_access_to_delete_message = request.user.has_perm("messenger_app.give_access_to_delete_message")
    give_access_to_chat = request.user.has_perm("messenger_app.give_access_to_chat")
    context = {
        "messages": messages,
        "title": "Messenger",
        "give_access_to_delete_message": give_access_to_delete_message,
        "give_access_to_chat": give_access_to_chat,
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


@login_required
@require_POST
def remove_text(request, text_id):
    text = get_object_or_404(UserMessage, id=text_id)
    if text.can_delete(request.user):
        text.delete()
    return redirect(request.META.get("HTTP_REFERER", "index"))


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


@login_required
def logout(request):
    auth.logout(request)
    return redirect('index')
