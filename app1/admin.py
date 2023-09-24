from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app1.models import job, Contact
from django.contrib.auth.models import User
from django.conf import settings

# Register your models here.

class job_admin(admin.ModelAdmin):
    list_display = [field.name for field in job._meta.get_fields() if not field.many_to_many]
    list_filter =  ['id', 'salary', 'vacancies', 'published_date', 'last_date', 'yop']
    search_fields = ['id','role', 'company_name', 'category', 'salary', 'yop', 'job_location', 'qualification']
    list_display_links = [field.name for field in job._meta.get_fields() if not field.many_to_many]
    list_select_related = True
    list_per_page = settings.LIST_PER_PAGE
    list_max_show_all = settings.LIST_MAX_SHOW_ALL
    # list_display = [field.name for field in job._meta.get_fields()]
    # list_filter = [field.name for field in job._meta.get_fields()]
    # date_hierarchy = ['published_date', 'last_date', 'last_modified']
    # list_editable = ['id'] 

admin.site.register(job, job_admin)
admin.site.site_header = "JobPulse Admin Panel"
admin.site.site_title = "Job"
admin.site.index_title = "Welcome To JobPulse Admin Panel"


class Contact_admin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.get_fields()]
    list_filter =  ['id', 'post_date']
    list_display_links = [field.name for field in Contact._meta.get_fields()]
    date_hierarchy = 'post_date'
    list_select_related = ['user_name']
    list_per_page = settings.LIST_PER_PAGE
    list_max_show_all = settings.LIST_MAX_SHOW_ALL
    # list_editable = ['user_name'] 
    # search_fields = ['id','user_name', 'first_name', 'last_name', 'email_id']

admin.site.register(Contact, Contact_admin)
admin.site.site_header = "JobPulse Admin Panel"
admin.site.site_title = "Contact"
admin.site.index_title = "Welcome To JobPulse Admin Panel"


class DjangoUser(User):
    class Meta:
        proxy = True

@admin.register(DjangoUser)
class MetaUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'is_authenticated', 'is_staff', 'is_active','date_joined', 'last_login']
    list_filter = ['first_name', 'last_name', 'email', 'is_staff', 'is_active','date_joined', 'last_login']
    search_fields = ['id', 'first_name', 'last_name', 'email']
    list_display_links = ['username', 'first_name', 'last_name', 'email']
    date_hierarchy = 'last_login'
    list_select_related = True
    list_per_page = settings.LIST_PER_PAGE
    list_max_show_all = settings.LIST_MAX_SHOW_ALL
