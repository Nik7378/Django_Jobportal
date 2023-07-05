from django.urls import path
from .import views
from django.urls import re_path


urlpatterns = [

    # html templates
    path('', views.index_page, name="index_page"),
    path('index', views.index_page, name="index_page"),
    path('feedback', views.feedback_page, name="feedback_page"),
    path('about', views.about_page, name="about_page"),
    path('contact', views.contact_page, name="contact_page"),
    path('signuppage', views.signup_page, name="signup_page"),
    path('loginpage', views.login_page, name="login_page"),
    path('feedback', views.feedback_page, name="feedback_page"),
    # path('admin', views.handlelogin, name="login"),

    # user operations views
    path('login', views.handle_login, name="handle_login"),
    path('logout', views.handle_logout, name="handle_logout"),
    path('signup', views.handle_signup, name="handle_signup"),
    path('userprofile/<str:slug>', views.user_profile, name="user_profile"),
    path('userdetails/<str:slug>', views.user_details, name="user_details"),
    path('changepass', views.change_user_passwd, name="change_user_passwd"),
    path('userresetpass', views.reset_user_passwd, name="reset_user_passwd"),

    # job operations views
    path('add', views.add_job, name="add_job"),
    path('edit/<str:slug>', views.edit_job, name="edit_job"),
    path('delete/<str:slug>', views.delete_job, name="delete_job"),
    path('alljob', views.view_all_jobs, name="view_all_jobs"),
    path('searchjob', views.search_job, name="search_job"),
    path('filterbybatch', views.filter_job_by_batch, name="filter_job_by_batch"),
    path('filterbylocation', views.filter_job_by_location, name="filter_job_by_location"),
    path('filterbydegree', views.filter_job_by_degree, name="filter_job_by_degree"),
    path('sortbydate', views.sort_job_by_date, name="sort_job_by_date"),
    path('favouritejob/<str:slug>', views.favourite_job, name="favourite_job"),
    path('favouritejoblist', views.favourite_joblist, name="favourite_joblist"),
    path('getjob/<str:slug>', views.get_job, name="get_job"),
    path('filterjob', views.filter_job_page, name="filter_job_page"),

]