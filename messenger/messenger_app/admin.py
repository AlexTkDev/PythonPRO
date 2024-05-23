from django.contrib import admin
from .models import UserMessage
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserMessageInline(admin.TabularInline):
    model = UserMessage
    extra = 0
    can_delete = True


class UserAdmin(BaseUserAdmin):
    inlines = [UserMessageInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'date_sent')
    list_filter = ('author', 'date_sent')
    date_hierarchy = 'date_sent'
    search_fields = ('author__username', 'message')


admin.site.register(UserMessage, UserMessageAdmin)
