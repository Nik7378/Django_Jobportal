from django.db import models
from django.contrib.auth.models import User 
from autoslug import AutoSlugField

# Create your models here.

class jobmanager(models.Manager):
    def sort_by_date(x):
        return x.order_by('-last_modified')
    
class job(models.Model):

    exp_ch =[ 
        ('Select experience', 'Select experience'),
        ('0','0'), #(value,label)
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('3+', '3+')
    ]

    location_ch=[
        ('Select job location', 'Select job location'),
        ('Mumbai','Mumbai'),
        ('Pune','Pune'),
        ('Navi mumbai','Navi Mumbai'),
        ('Thane','Thane'),
        ('Andheri','Andheri')
    ]

    job_cat = [
        ('Select job category', 'Select job category'),
        ('Entry Level','Entry-Level'),
        ('Mid level','Mid-Level'),
        ('Senior Level','Senior-Level')
    ]

    job_role = [
        ('Select job role', 'Select job role'),
        ('App developer','App developer'), 
        ('Database administrator','Database administrator'), 
        ('Service desk analyst','Service desk analyst'), 
        ('Software developer','Software developer'), 
        ('Software engineer','Software engineer'), 
        ('Software tester','Software tester'), 
        ('Web developer','Web developer') 
    ]

    job_degree = [
        ('Select degree', 'Select degree'),
        ('Any Degree','Any Degree'),
        ('M.E/M.Tech/M.S','M.E/M.Tech/M.S'),
        ('B.E/B.Tech','B.E/B.Tech'),
        ('MBA','MBA'),
        ('Diploma','Diploma'),
    ]
    
    job_id = models.CharField(max_length=10)
    role = models.CharField(default=job_role, max_length=50, choices=job_role)
    company_name = models.CharField(max_length=50)
    company_site = models.URLField(max_length=200)
    category = models.CharField(max_length=50, choices=job_cat, default=job_cat)
    salary = models.FloatField()
    yop = models.CharField(max_length=50)
    job_location = models.CharField(max_length=50, choices=location_ch, default=location_ch)
    qualification = models.CharField(max_length=50, choices=job_degree, default=job_degree)
    #specialization = models.CharField(max_length=50, choices=)
    vacancies = models.IntegerField()
    experience = models.CharField(max_length=50, choices=exp_ch, default=exp_ch)
    drive_location = models.CharField(max_length=100)
    venue_details = models.TextField(max_length=200, blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateField()
    apply_link = models.URLField(max_length=200)
    last_modified = models.DateTimeField(auto_now_add = True)
    publisher_name = models.CharField(max_length=50)
    updated_by = models.CharField(max_length=50, default=None)
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    views = models.IntegerField(default=0)
    #slug = models.CharField(max_length=200, unique=True, null=False, default='', editable=False)
    slug = AutoSlugField(populate_from = 'role', max_length=200, unique=True, null=True, editable=False)
    objects = models.Manager()
    jb_manager = jobmanager()


class Contact(models.Model):
    #user_name = models.CharField(max_length=10)
    # user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_name = models.ForeignKey(User, on_delete=models.PROTECT)
    # user_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    user_name = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="Guest")
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()