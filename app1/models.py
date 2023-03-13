from django.db import models

# Create your models here.

class jobmanager(models.Manager):
    def sort_by_date(x):
        return x.order_by('-published_date')
    
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
    objects = models.Manager()
    jb_manager = jobmanager()
