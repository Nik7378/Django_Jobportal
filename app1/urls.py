from django.urls import path
from .import views
from django.urls import re_path


urlpatterns = [

    # html templates
    path('jobpulse', views.index_page, name="index_page"),
    path('jobpulse/index', views.index_page, name="index_page"),
    path('jobpulse/feedback', views.feedback_page, name="feedback_page"),
    path('jobpulse/about', views.about_page, name="about_page"),
    path('jobpulse/contact', views.contact_page, name="contact_page"),
    path('jobpulse/signuppage', views.signup_page, name="signup_page"),
    path('jobpulse/loginpage', views.login_page, name="login_page"),
    path('jobpulse/feedback', views.feedback_page, name="feedback_page"),
    # path('admin', views.handlelogin, name="login"),

    # user operations views
    path('jobpulse/login', views.handle_login, name="handle_login"),
    path('jobpulse/logout', views.handle_logout, name="handle_logout"),
    path('jobpulse/signup', views.handle_signup, name="handle_signup"),
    path('jobpulse/userprofile/<str:slug>', views.user_profile, name="user_profile"),
    path('jobpulse/userdetails/<str:slug>', views.user_details, name="user_details"),
    path('jobpulse/changepass', views.change_user_passwd, name="change_user_passwd"),
    path('jobpulse/userresetpass', views.reset_user_passwd, name="reset_user_passwd"),

    # job operations views
    path('jobpulse/add', views.add_job, name="add_job"),
    path('jobpulse/edit/<str:slug>', views.edit_job, name="edit_job"),
    path('jobpulse/delete/<str:slug>', views.delete_job, name="delete_job"),
    path('jobpulse/alljob', views.view_all_jobs, name="view_all_jobs"),
    path('jobpulse/searchjob', views.search_job, name="search_job"),
    path('jobpulse/filterbybatch', views.filter_job_by_batch, name="filter_job_by_batch"),
    path('jobpulse/filterbylocation', views.filter_job_by_location, name="filter_job_by_location"),
    path('jobpulse/filterbydegree', views.filter_job_by_degree, name="filter_job_by_degree"),
    path('jobpulse/sortbydate', views.sort_job_by_date, name="sort_job_by_date"),
    path('jobpulse/favouritejob/<str:slug>', views.favourite_job, name="favourite_job"),
    path('jobpulse/favouritejoblist', views.favourite_joblist, name="favourite_joblist"),
    path('jobpulse/getjob/<str:slug>', views.get_job, name="get_job"),
    path('jobpulse/filterjob', views.filter_job_page, name="filter_job_page"),

]