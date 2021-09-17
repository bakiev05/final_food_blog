from django.views import generic
from apps.blog import models


class HomeView(generic.ListView):
    model = models.Post
    paginate_by = 9
    template_name = 'blog/home.html'


class PostListView(generic.ListView):
    model = models.Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return models.Post.objects.filter(
            category__slug=self.kwargs.get("slug")
        ).select_related('category')


class PostDetailView(generic.DetailView):
    model = models.Post
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = "post"


