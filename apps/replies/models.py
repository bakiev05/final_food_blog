from django.db import models
from apps.blog.models import Post
from apps.users.models import User


class Reply(models.Model):
    text = models.TextField(
        verbose_name='reply_text'
    )
    user = models.ForeignKey(
        User,
        related_name='reply_user',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name='reply_post',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.post.id} -- {self.user.id}"
