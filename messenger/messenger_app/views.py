from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from .models import UserMessage
from .form import UserLoginForm, UserRegistrationForm
from .mixins import (
    CustomLoginRequiredMixin,
    CanEditMessageMixin,
    CanDeleteMessageMixin,
    FormInvalidMessageMixin,
    RedirectIfAuthenticatedMixin,
    ActiveUserRequiredMixin,
    UserIsAuthorMixin,
    SuperuserRequiredMixin,
    AdminOnlyMixin,
    OwnerOrAdminMixin,
    StaffRequiredMixin
)


class IndexView(CustomLoginRequiredMixin, ActiveUserRequiredMixin, View):
    def get(self, request):
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


class SaveTextView(CustomLoginRequiredMixin, ActiveUserRequiredMixin, FormInvalidMessageMixin, View):
    error_message = "Сообщение не может быть пустым."

    def post(self, request):
        message_text = request.POST.get("message_text", "")
        if message_text:
            UserMessage.objects.create(message=message_text, author=request.user)
            return redirect('index')
        else:
            messages = UserMessage.objects.all().order_by('-date_sent')
            context = {
                "messages": messages,
                "error": self.error_message,
                "title": "Messenger"
            }
            return render(request, "messenger_app/index.html", context)

    def get(self, request):
        return redirect('index')


class EditTextView(CustomLoginRequiredMixin, ActiveUserRequiredMixin, CanEditMessageMixin, View):
    def get_object(self):
        text_id = self.kwargs.get("text_id")
        return get_object_or_404(UserMessage, id=text_id)

    def get(self, request, text_id):
        message = self.get_object()
        context = {
            "message": message,
            "title": "Редактировать сообщение"
        }
        return render(request, "messenger_app/edit_text.html", context)

    def post(self, request, text_id):
        message = self.get_object()
        new_message_text = request.POST.get("message_text", "")
        if new_message_text:
            message.message = new_message_text
            message.save()
            return redirect('index')
        else:
            context = {
                "message": message,
                "error": "Сообщение не может быть пустым.",
                "title": "Редактировать сообщение"
            }
            return render(request, "messenger_app/edit_text.html", context)


@method_decorator(login_required, name='dispatch')
@method_decorator(require_POST, name='dispatch')
class RemoveTextView(CustomLoginRequiredMixin, CanDeleteMessageMixin, View):
    def get_object(self):
        text_id = self.kwargs.get("text_id")
        return get_object_or_404(UserMessage, id=text_id)

    def post(self, request, text_id):
        text = self.get_object()
        if text.can_delete(request.user):
            text.delete()
        return redirect(request.META.get("HTTP_REFERER", "index"))


class LoginView(RedirectIfAuthenticatedMixin, View):
    def get(self, request):
        form = UserLoginForm()
        context = {"form": form, "title": "Авторизация"}
        return render(request, "messenger_app/login.html", context)

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('index')
        context = {"form": form, "title": "Авторизация", "error": "Форма заполнена неверно."}
        return render(request, "messenger_app/login.html", context)


class RegisterView(RedirectIfAuthenticatedMixin, View):
    def get(self, request):
        form = UserRegistrationForm()
        context = {"form": form, "title": "Регистрация"}
        return render(request, "messenger_app/register.html", context)

    def post(self, request):
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context = {"form": form, "title": "Регистрация", "error": "Форма заполнена неверно."}
        return render(request, "messenger_app/register.html", context)


class LogoutView(CustomLoginRequiredMixin, ActiveUserRequiredMixin, View):
    def get(self, request):
        auth.logout(request)
        return redirect('index')
