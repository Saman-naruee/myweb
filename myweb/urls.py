from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
import debug_toolbar
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(('blog.urls', 'blog'))),
    path('polls/', include(('polls.urls', 'polls'))), 
    # path('__debug__/', include(debug_toolbar.urls)),
] + debug_toolbar_urls()

