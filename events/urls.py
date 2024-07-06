from django.urls import path
from . import views
app_name = 'events'
urlpatterns = [
    path('events/upcoming/', views.upcoming_events, name='events'),
]
