from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['Title', 'status', 'Publish', 'Author']
    ordering = ('Title', 'Publish')
    list_filter = ['Author', 'status']
    search_fields = ['Title', 'Description']
    # raw_id_fields = ['Author']
    date_hierarchy = 'Publish'
    prepopulated_fields = {'Slug': ('Title',)}
    list_editable =['status']
    # list_display_links = ['Author']
    