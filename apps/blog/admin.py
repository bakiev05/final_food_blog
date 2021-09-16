from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from apps.blog import models
from apps.replies.models import Reply
from apps.users.models import User
from apps.categories.models import Category


class PostImageInline(admin.StackedInline):
    model = models.PostImage
    extra = 1


class RecipeVideoInline(admin.StackedInline):
    model = models.RecipeVideo
    extra = 1


class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'category', 'create_at', 'id']
    inlines = [PostImageInline, RecipeInline]


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'cook_time', 'ingredients', 'post', 'process']
    inlines = [RecipeVideoInline]


admin.site.register(User)
admin.site.register(models.RecipeVideo)
admin.site.register(models.PostImage)

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Reply)
admin.site.register(models.Like)
admin.site.register(models.Tag)
