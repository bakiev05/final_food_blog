from django.test import TestCase, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from unittest import mock
from django.test import Client
from apps.blog.views import HomeView
from apps.categories.models import Category
from apps.blog.models import Post, Recipe, Tag

User = get_user_model()


class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        self.category = Category.objects.create(title='Dinner', slug='dinner')
        self.tag = Tag.objects.create(name='vegan', slug='vegan')
        self.post = Post.objects.create(
            author=self.user,
            title='dinner',
            tags=self.tag,
            slug='dinner',
            category=self.category,
        )
        self.recipe = Recipe.objects.create(
            title='tile recipe',
            cook_time=20,
            ingredients='sd sad sa dsad dsa ds',
            post=self.post,
            process='a lot of time',
        )

    def test_mock_homepage(self):
        mock_data = mock.Mock(status_code=200)
        with mock.patch('apps.blog.views.HomeView.get', return_value=mock_data) as mock_data:
            factory = RequestFactory()
            request = factory.get('')
            response = HomeView.as_view()(request)
            self.assertEqual(response.status_code, 200)

    def test_get_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_detail(self):
        post = Post.objects.first()
        url = reverse('post_detail', kwargs={'pk': post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, HomeView.as_view())