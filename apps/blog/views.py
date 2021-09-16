from django.shortcuts import render
from django.views import generic
from apps.blog import models


class PostListView(generic.ListView):
    model = models.Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return models.Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


def data(request):
    return render(request, 'index.html')