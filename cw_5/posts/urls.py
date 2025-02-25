from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/posts/', permanent=False), name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/my/', views.my_posts, name='my_posts'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/new/', views.post_create, name='post_create'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    # Optional: Thread management URLs
    path('threads/', views.thread_list, name='thread_list'),
    path('threads/new/', views.thread_create, name='thread_create'),
]