from django import template
from apps.categories.models import Category
from apps.blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    category = Category.objects.all()
    return {"list_category": category}


@register.inclusion_tag('blog/include/tags/recipes_tag.html')
def get_last_posts():
    posts = Post.objects.select_related('category').order_by("-id")[:5]
    return {"list_last_post": posts}
