from django.urls import path
from apps.blog import views

urlpatterns = [
    path('', views.data, name='data'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
]
