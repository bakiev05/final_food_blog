from django.views import generic
from apps.blog import models
from apps.replies.forms import ReplyForm
from apps.replies.models import Reply


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReplyForm()
        return context


class CreateReply(generic.CreateView):
    model = Reply
    form_class = ReplyForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()