from django.test import TestCase, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
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
            slug='dinner',
            category=self.category,
            image=SimpleUploadedFile('post_image.jpg', content=b'', content_type='image/jpg')
        )
        self.recipe = Recipe.objects.create(
            title='tile recipe',
            cook_time=20,
            ingredients='sd sad sa dsad dsa ds',
            post=self.post,
            process='a lot of time',
        )
        return super().setUp()

    def test_get_home_url(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_list_url(self):
        url = reverse('post_list', args=['some_slug'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def post_detail_url(self):
        url = reverse('post_detail', kwargs={'some_slug': 'post_slug'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
