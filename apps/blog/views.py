from django.views import generic
from apps.blog import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.forms import inlineformset_factory
from apps.replies.forms import ReplyForm
from apps.replies.models import Reply
from apps.blog.forms import PostForm, RecipeForm


class HomeView(generic.ListView):
    model = models.Post
    paginate_by = 9
    template_name = 'blog/home.html'


class PostListView(generic.ListView):
    model = models.Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'
    paginate_by = 9

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


def create_post(request):
    form = PostForm(request.POST, request.FILES, None)
    RecipeFormSet = inlineformset_factory(models.Post, models.Recipe, form=RecipeForm, extra=1)
    if form.is_valid():
        post = models.Post()
        post = form.save(commit=False)
        post.author = request.user
        post.description = form.cleaned_data['description']
        post.save()
        formset = RecipeFormSet(request.POST, request.FILES, instance=post)
        if formset.is_valid():
            formset.save()
            return redirect('home')
    formset = RecipeFormSet()
    return render(request, 'blog/post_create.html', locals())


def update_post(request, id):
    post = get_object_or_404(models.Post, id=id)
    form = PostForm(request.POST, request.FILES, None, instance=post)
    RecipeFormSet = inlineformset_factory(models.Post, models.Recipe, form=RecipeForm, extra=0)
    if request.user == post.author:
        if form.is_valid():
            post.author = request.user
            post = form.save()
            formset = RecipeFormSet(request.POST, request.FILES, instance=post)
            if formset.is_valid():
                formset.save()
                return redirect('home')
        formset = RecipeFormSet(instance=post)
    return render(request, 'blog/post_update.html', locals())


@login_required
def delete_post(request, id):
    if request.method == 'POST':
        post = models.Post.objects.get(id=id)
        recipe = models.Recipe.objects.get(id=id)
        if request.user == post.author:
            post.delete()
            recipe.delete()
        return redirect('home')
    return render(request, 'blog/post_delete.html', locals())
