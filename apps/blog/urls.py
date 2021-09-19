from django.urls import path
from apps.blog import views
from apps.contact.views import ContactView, AboutView, CreateContact

urlpatterns = [
    path('contact/', ContactView.as_view(), name="contact"),
    path('about/', AboutView.as_view(), name="about"),
    path('feedback/', CreateContact.as_view(), name="feedback"),
    path('reply/<int:pk>/', views.CreateReply.as_view(), name='create_reply'),
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),

    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
]
