from django.db import models
from django.contrib.auth.models import AbstractUser


class CommentUser(AbstractUser):
    image = models.ImageField(
        upload_to='media/user_picture',
        default='media/user_picture/bill-gates-profile-pic.jpg',
        null=True,
        blank=True
    )

    @property
    def get_user_info(self):
        return {
            'username': self.username,
            'full_name': self.first_name + ' ' + self.last_name,
            'image_url': self.image.url
        }