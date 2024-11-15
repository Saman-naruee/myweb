from django.urls import path
from . import views
from django.urls import include, path
from django.contrib import admin

app_name = 'polls'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path("<int:pk>/", views.DetailsView.as_view(), name='detail'),
    path("<int:pk>/results/", views.ResultsView.as_view(), name='results'),
    path("<int:question_id>/vote/", views.vote, name='vote'),
    path("learning", views.learning, name='learning')
]

