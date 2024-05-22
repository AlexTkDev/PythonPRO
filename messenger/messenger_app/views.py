from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import UserMessage


# Create your views here.
def index(request):
    messages = UserMessage.objects.all().order_by('-date_sent')
    context = {
        "messages": messages,
        "title": "Messenger",
    }
    return render(request, "messenger_app/base.html", context)


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
            return render(request, "messenger_app/base.html", context)
    return redirect('index')
