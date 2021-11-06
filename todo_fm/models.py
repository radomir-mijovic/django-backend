from django.db import models


class Todos(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    completed = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.name)
