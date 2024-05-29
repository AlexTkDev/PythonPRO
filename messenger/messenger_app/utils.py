from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


class SuperuserRequiredMixin:
    """Проверка, является ли пользователь суперпользователем."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ActiveUserRequiredMixin:
    """Проверяет, что пользователь активен (учетная запись не заблокирована)."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_active:
            raise PermissionDenied("Учетная запись пользователя заблокирована.")
        return super().dispatch(request, *args, **kwargs)


class CanEditMessageMixin:
    """Может ли пользователь редактировать сообщение."""
    def dispatch(self, request, *args, **kwargs):
        message = self.get_object()
        if not message.can_edit(request.user):
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class CanDeleteMessageMixin:
    """Может ли пользователь удалять сообщение."""
    def dispatch(self, request, *args, **kwargs):
        message = self.get_object()
        if not message.can_delete(request.user):
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class FormInvalidMessageMixin:
    """Добавление сообщения об ошибке при неверной форме."""
    error_message = "Форма заполнена неверно."

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context['error'] = self.error_message
        return self.render_to_response(context)


class RedirectIfAuthenticatedMixin:
    """Перенаправление аутентифицированных пользователей на главную страницу."""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class UserIsAuthorMixin:
    """Проверка, является ли пользователь автором сообщения."""
    def dispatch(self, request, *args, **kwargs):
        message = self.get_object()
        if message.author != request.user:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class CustomLoginRequiredMixin(LoginRequiredMixin):
    """Замена LoginRequiredMixin для указания login_url по умолчанию."""
    login_url = 'login'


class AdminOnlyMixin(PermissionRequiredMixin):
    """Проверка, является ли пользователь администратором."""
    permission_required = 'is_superuser'


class OwnerOrAdminMixin:
    """Является ли пользователь владельцем сообщения или администратором."""
    def dispatch(self, request, *args, **kwargs):
        message = self.get_object()
        if message.author != request.user and not request.user.is_superuser:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class StaffRequiredMixin:
    """Проверка, является ли пользователь сотрудником (staff)."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied("Доступ разрешен только для сотрудников.")
        return super().dispatch(request, *args, **kwargs)
