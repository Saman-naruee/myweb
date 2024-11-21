from django.urls import path
from .views import PostListView
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('posts/', PostListView, name = 'post_list'),
    path('posts/<pk>', views.PostDetailView.as_view(), name = 'post_detail'),
    path('ticket/', views.ticket, name = 'ticket'),
]
