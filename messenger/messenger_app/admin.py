from django.contrib import admin
from .models import UserMessage


# Register your models here.


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'date_sent')
    list_filter = ('author', 'date_sent')
    date_hierarchy = 'date_sent'
    search_fields = ('author__username', 'message')


admin.site.register(UserMessage, UserMessageAdmin)
