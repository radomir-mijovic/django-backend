from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CommentUser


class CommentUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'image']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('image',)}),
    )


admin.site.register(CommentUser, CommentUserAdmin)
