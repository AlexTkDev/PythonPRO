from django.contrib import admin
from members_app.models import Member

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', "save_text")
    search_fields = ('id', "save_text")


admin.site.register(Member, MemberAdmin)
