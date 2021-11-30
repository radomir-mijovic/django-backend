from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class ProductFeedback(models.Model):
    status_choice = [
        ('Suggestion', 'Suggestion'),
        ('Planned', 'Planned'),
        ('In-Progress', 'In-Progress'),
        ('Live', 'Live')
    ]

    title = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=400, null=True, blank=True)
    up_votes = models.IntegerField(default=0, null=True, blank=True)
    status = models.CharField(max_length=100, choices=status_choice, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-up_votes']


class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(ProductFeedback, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.text)


class Replies(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='replies')
    reply = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.comment.text + self.reply)
