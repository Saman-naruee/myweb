from django.contrib import admin
from django.urls import path, include
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(('blog.urls', 'blog'))),
    path('polls/', include(('polls.urls', 'polls'))), 
] 