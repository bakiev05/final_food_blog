from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from django.urls import reverse
from apps.users.models import User
from apps.categories.models import Category


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='user_post'
    )
    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="post",
        blank=True
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        null=True, blank=True
    )
    slug = models.SlugField(
        max_length=200,
        unique=True
    )

    category = models.ForeignKey(
        Category,
        related_name='post_category',
        on_delete=models.SET_NULL,
        null=True
    )
    image = models.FileField(
        upload_to='post_image',
        blank=True, null=True
    )

    class Meta:
        ordering = ('-id',)

    def get_recipes(self):
        return self.recipe.all()

    def get_user_profile(self):
        return self.user_post.all()

    def get_reply(self):
        return self.reply_post.all()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.category.slug, 'post_slug': self.slug})

    def __str__(self):
        return f"{self.title}"


class Recipe(models.Model):
    title = models.CharField(
        max_length=100
    )
    cook_time = models.PositiveIntegerField(
        default=0
    )
    ingredients = RichTextField()
    post = models.ForeignKey(
        Post,
        related_name="recipe",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    process = RichTextField(
        blank=True,
        null=True
    )
    video = models.FileField(
        upload_to='videos/',
        null=True, blank=True,
    )

    def __str__(self):
        return f'{self.title}'


# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_user')
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes_post')
#
#     def __str__(self):
#         return f"{self.user.username} -- {self.post.title}"
