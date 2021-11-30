from django.contrib import admin
from .models import *


class ProductFeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'up_votes', 'status', 'description']


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'product', 'user']


class RepliesAdmin(admin.ModelAdmin):
    list_display = ['id', 'reply', 'comment', 'user']


admin.site.register(ProductFeedback, ProductFeedbackAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Replies, RepliesAdmin)
