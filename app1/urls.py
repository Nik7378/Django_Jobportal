from django.urls import path
from .import views


urlpatterns = [
    path('alljob', views.view_all_jobs, name="viewall"),
    path('add', views.add_job, name="add"),
    path('edit/<rid>', views.edit_job, name="edit"),
    path('delete/<rid>', views.delete_job, name="delete"),
    path('filterbybatch', views.filterbybatch, name="filterbybatch"),
    path('filterbylocation', views.filterbylocation, name="filterbylocation"),
    path('filterbydegree', views.filterbydegree, name="filterbydegree"),
    path('sortbydate', views.sortbydate, name="sortbydate"),
    path('getjob/<rid>', views.get_job, name="getjob"),
    path('search', views.search_job, name="searchjob"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('', views.index, name="index")

]
