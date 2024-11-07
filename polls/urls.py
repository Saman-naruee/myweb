from django.urls import path
from . import views
from django.urls import include, path
from django.contrib import admin

app_name = 'polls'

urlpatterns = [
    path("", views.index, name="index"),
    path('admin/', admin.site.urls),
    path("<int:question_id>/", views.detail, name='detail'),
    path("<int:question_id>/results/", views.results, name='results'),
    path("<int:question_id>/vote/", views.vote, name='vote'),
    path("learning", views.learning, name='learning')
]

# app_name = "polls"
# urlpatterns = [
#     path("", views.IndexView.as_view(), name="index"),
#     path("<int:pk>/", views.DetailView.as_view(), name="detail"),
#     path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
#     path("<int:question_id>/vote/", views.vote, name="vote"),
#     ]
