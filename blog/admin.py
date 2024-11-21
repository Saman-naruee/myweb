from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter

# You need to import this for adding jalali calendar widget
import django_jalali.admin as jadmin

# admin.sites.AdminSite.site_header = 'پنل مدیریت جنگو'
# admin.sites.AdminSite.site_title = 'Admin'
# admin.sites.AdminSite.index_title = 'مدیریت جنگو'



# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['Title', 'status', 'Publish', 'Author']
    ordering = ('Title', 'Publish')
    list_filter = ['Author', 'status', ('Publish', JDateFieldListFilter)]
    search_fields = ['Title', 'Description']
    # raw_id_fields = ['Author']
    date_hierarchy = 'Publish'
    prepopulated_fields = {'Slug': ('Title',)}
    list_editable =['status']
    # list_display_links = ['Author']

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'subject', 'phone']
    ordering = ('name', 'email')
    list_filter = ['name', 'email']
    search_fields = ['name', 'email', 'message']
