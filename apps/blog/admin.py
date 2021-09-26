from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from apps.blog import models
from apps.replies.models import Reply
from apps.users.models import User
from apps.categories.models import Category


class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'category', 'create_at', 'id']
    inlines = [RecipeInline]
    search_fields = ('title', 'category__title', 'author__username')
    list_filter = ('category', 'author')
    save_as = True
    save_on_top = True


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'cook_time', 'ingredients', 'post', 'process']
    search_fields = ('title', 'post__title',)
    list_filter = ('post',)


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post']
    search_fields = ('user__username', 'post__title',)
    list_filter = ('user', 'post')
    readonly_fields = ('user', 'post')


admin.site.register(User)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(models.Tag)
