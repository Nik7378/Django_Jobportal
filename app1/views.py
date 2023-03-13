from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import jobapply
from .models import job
#import datetime
from datetime import datetime


# Create your views here.

def index(request):
    content = {}
    content['data'] = job.objects.all()
    return render(request,'index.html', content)

def add_job(request):
    now = datetime.now()
    
    if request.method == 'POST':
        fm = jobapply(request.POST)
        if fm.is_valid():
            # print(fm)
            # fm.save()
            j1 = fm.save(commit=False)
            j1.last_modified = now
            j1.save()
            #fm.save_m2m()
            return redirect('/alljob')
    else:
        fm = jobapply()
    return render(request, "addjob.html", {'form':fm})

def edit_job(request, rid):
    now = datetime.now()
    # format = '%Y-%m-%d %H:%M %p'
    # d1 = now.strftime(format)

    j1 = job.objects.get(id=rid)
    if request.method == 'POST':
        fm  = jobapply(request.POST, instance=j1)
        if fm.is_valid():
            #fm.save()
            j2 = fm.save(commit=False)
            j2.last_modified = now
            j2.save()
            return redirect('/alljob')
    else:
        fm = jobapply(instance=j1)
    return render(request, 'edit_job.html', {'form': fm})

def get_job(request, rid):
    content = {}
    content['data'] = job.objects.get(id=rid)
    return render(request, 'getjob.html',content)

def search_job(request):
    content = {}
    content['data'] = job.objects.all()
    return render(request, 'searchjob.html',content)

def delete_job(request, rid):
    x = job.objects.get(id=rid)
    x.delete()
    return redirect('/alljob')

def view_all_jobs(request):
    content = {}
    content['data'] = job.objects.all()
    return render(request, 'dashboard.html',content)

def filterbybatch(request):
    if request.method == "GET":
        st=request.GET.get('batch')
        if st != None:
            content = {}
            content['data'] = job.objects.filter(yop__icontains=st)
    return render(request, 'searchjob.html',content)

def filterbylocation(request):
    if request.method == "GET":
        st=request.GET.get('joblocation')
        if st != None:
            content = {}
            content['data'] = job.objects.filter(job_location__icontains=st)
    return render(request, 'searchjob.html',content)

def filterbydegree(request):
    if request.method == "GET":
        st=request.GET.get('degree')
        if st != None:
            content = {}
            content['data'] = job.objects.filter(qualification__icontains=st)
    return render(request, 'searchjob.html',content)

def sortbydate(request):
    content = {}
    content['data'] = job.jb_manager.sort_by_date()
    return render(request, 'searchjob.html',content)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
