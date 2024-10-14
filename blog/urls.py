from django.urls import path
from .views import PostListView
from . import views
app_name = 'blog'

urlpatterns = [
            path('', PostListView, name = 'post_list'),
            path('posts/<pk>', views.PostDetailView.as_view(), name = 'post_detail'),
              ]