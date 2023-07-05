from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import jobapply, EditUserProfileForm, EditAdminProfileForm, ContactForm
from .models import job, Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
import datetime
from datetime import datetime
from django .core.paginator import Paginator
from django import template
from django.db.models import Sum, Count, Q, Max
import random
from django.conf import settings
import uuid

# Create your views here.

# def settings_export(request):
#     # context = {'captcha_key': settings.RECAPTCHA_PUBLIC_KEY}
#     context = "Hello"
#     return render(request, 'signup.html', context)

# Favourite job list 
@login_required(login_url="handle_login")
def favourite_joblist(request):
    if request.user.is_authenticated:
        content = job.objects.filter(favourites=request.user)
        paginator = Paginator(content, 5, orphans=1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'job/favourites.html', 
        {
            'page_obj': page_obj, 
            'total_jobs': job.objects.filter(favourites=request.user).count()
        })
    else:
        return render(request, 'error.html')


# Add or remove favorite job
@login_required(login_url="handle_login")
def favourite_job(request, slug):
    if request.user.is_authenticated:
        j1 = get_object_or_404(job, slug=slug)
        if j1.favourites.filter(id=request.user.id).exists():
            j1.favourites.remove(request.user) 
            messages.success(request, "Job removed from saved")
        else:
            j1.favourites.add(request.user) 
            messages.success(request, "Job saved")
        return redirect('favourite_joblist')
    else:
        return render(request, 'error.html')


# Home page with pagination
def index_page(request):
    content = job.objects.all().order_by('-last_modified')
    paginator = Paginator(content, 5, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', 
    {
        'page_obj': page_obj, 
        #'total_users': User.objects.filter(is_active=True).count(), or
        'total_users': User.objects.exclude(is_active=False).count(), 
        'total_jobs': job.objects.count(), 
        'companies': job.objects.order_by('company_name').values('company_name').distinct().count(),
        'total_vacancies' : job.objects.aggregate(Sum('vacancies'))['vacancies__sum']
        # 'trending' : job.objects.all().order_by('-views')[:3]
        #'trending' : job.objects.values('role').annotate(max_role=Max('role'))[:3]
    })


# User profile page
@login_required(login_url="handle_login")
def user_profile(request, slug):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)
                # request.user=slug
                users = None              
            if fm.is_valid():
                messages.success(request, "Your profile has been successfully updated")
                fm.save()
                return redirect('user_profile')
        else:     
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(instance=request.user)
                users = None
                return render(request, 'user/user_profile.html', {'form':fm, 'users': users})
            return render(request, 'user/admin_profile.html', {'form':fm, 'users': users})
    return render(request, 'error.html')
    #return redirect('user_profile')

# Change password page for users 
@login_required(login_url="handle_login")
def change_user_passwd(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                messages.success(request, "Your password has been successfully updated")
                fm.save()
                update_session_auth_hash(request, fm.user)
                return redirect('user_profile')
        else:        
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'user/change_user_pass.html', {'form':fm})
    # return render(request, 'error.html')
    return redirect('handle_login')


# Reset password without old password
@login_required(login_url="handle_login")
def reset_user_passwd(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                messages.success(request, "Your password has been successfully updated")
                fm.save()
                update_session_auth_hash(request, fm.user)
                return redirect('user_profile')
        else:        
            fm = SetPasswordForm(user=request.user)
        return render(request, 'user/resetpass.html', {'form':fm})
    # return render(request, 'error.html')
    return redirect('handle_login')


# User profile details page
@login_required(login_url="handle_login")
def user_details(request, slug):
    if request.user.is_authenticated and request.user.is_superuser:
        pi = User.objects.get(username=slug)
        fm = EditAdminProfileForm(instance=pi)
        return render(request, 'user/userdetail.html', {'form':fm, 'user':pi})
    else:
        return render(request, 'error.html')
  

# Load signup page
def signup_page(request):
    if request.user.is_authenticated:
        return redirect('index_page')
    else:
        return render(request, 'user/signup.html')


# Signup page process for new users
def handle_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return render( request, 'user/signup.html')

        # if not username.isalnum():
        #     messages.error(request, "Username must be combination of numbers and characters")
        #     return render( request, 'user/signup.html')
            
        if pass1 != pass2: 
            messages.error(request, "Password and confirm password does not matched")
            return render( request, 'user/signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "This username has already existed")
            return render( request, 'user/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists")
            return render( request, 'user/signup.html')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Congratuations, your account has been successfully created")
        return redirect('login_page')
    else:
        return redirect('signup_page')
      
# Load login page
def login_page(request):
    if request.user.is_authenticated:
        return redirect('index_page')
    else:
        return render(request, 'user/login.html')

# Login page process
def handle_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            request.session['email'] = email
            login(request, user)
            # return HttpResponse("Login Success")
            #v = request.session.get('email')
            #return render(request, 'header.html', {'value':v})
            messages.success(request, "Login Success")
            return redirect('index_page')
        else:
            # return HttpResponse("Login Failed")
            messages.error(request, "Please enter the correct username and password. try again")
            return redirect('login_page')
            
    #return HttpResponse("404 - Not Found")
    return redirect('login_page')

# Logout for loggedin users
@login_required(login_url="handle_login")
def handle_logout(request):
    if 'email' in request.session:
        del request.session['email']
    logout(request)
    messages.success(request, "Logout Success")
    return redirect('login_page')


# Add a new job to portal only for admin and staff
@login_required(login_url="handle_login")
def add_job(request):
    if request.user.is_superuser or request.user.is_staff:
        now = datetime.now()
        x = uuid.uuid4()
        publisher = request.user.username
        if request.method == 'POST':
            fm = jobapply(request.POST)
            if fm.is_valid():
                # print(fm)
                # fm.save()
                j1 = fm.save(commit=False)
                j1.publisher_name = publisher
                j1.updated_by = "To Be Updated"
                j1.last_modified = now
                j1.slug = j1.role +"_"+ str(x)
                j1.save()
                #fm.save_m2m()
                messages.success(request, "Congratuations, new job successfully added")
                return redirect('view_all_jobs')
        else:
            fm = jobapply()
        return render(request, "job/addjob.html", {'form':fm})
    else:
        return render(request, 'error.html')


# Edit job page only for admin and staff
@login_required(login_url="handle_login")
def edit_job(request, slug):
    if request.user.is_superuser or request.user.is_staff:
        now = datetime.now()
        x = uuid.uuid4()
        # format = '%Y-%m-%d %H:%M %p'
        # d1 = now.strftime(format)
        updated_by = request.user.username

        j1 = job.objects.get(slug=slug)
        if request.method == 'POST':
            fm  = jobapply(request.POST, instance=j1)
            if fm.is_valid():
                #fm.save()
                j2 = fm.save(commit=False)
                j2.last_modified = now
                j2.updated_by = updated_by
                j2.slug = j2.role +"_"+ str(x)
                j2.save()
                messages.success(request, "Congratuations, job has been successfully updated")
                return redirect('view_all_jobs')
        else:
            fm = jobapply(instance=j1)
        return render(request, 'job/edit_job.html', {'form': fm})
    else:
        return render(request, 'error.html')


# Show single jobs detail to users
def get_job(request, slug):
    j1 = get_object_or_404(job, slug=slug)
    fav = bool
    j1.views = j1.views + 1
    request.session['count'] = j1.views
    j1.save()

    if j1.favourites.filter(id=request.user.id).exists():
        fav = True 
    if request.user.is_authenticated and request.user.is_superuser == True:
        users = User.objects.filter(username=j1.publisher_name)
        users2 = User.objects.filter(username=j1.updated_by)
    else:
        users = None
        users2 = None
    return render(request, 'job/getjob.html',{
        'data': job.objects.get(slug=slug),
        'fav' : fav,
        'users': users,
        'users2': users2
    })


# Filter job page for all users
def filter_job_page(request):
    content = {}
    content['data'] = job.objects.all()
    content['total_jobs'] = job.objects.all().count()
    return render(request, 'job/filterjob.html',content)


# Delete job only for admin and staff
@login_required(login_url="handle_login")
def delete_job(request, slug):
    if request.user.is_superuser or request.user.is_staff:
        x = job.objects.get(slug=slug)
        x.delete()
        messages.success(request, "Congratuations, job has been successfully deleted")
        return redirect('view_all_jobs')
    else:
        return render(request, 'error.html')


# View all jobs on Dashboard in detail
def view_all_jobs(request):
    content = job.objects.all().order_by('-last_modified')
    paginator = Paginator(content, 5, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'job/dashboard.html', {'page_obj': page_obj, "total_jobs": job.objects.count()})


# Search job by title or company
def search_job(request):
    if request.method == "GET":
        st_tc = request.GET.get('searchbytc')
        st_location = request.GET.get('searchbylocation')
        st_type = request.GET.get('searchbytype')

        if len(st_tc)>70:
            content = job.objects.none()
            paginator = Paginator(content, 100, orphans=1)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            total_jobs = content.count()

        elif st_tc != None and st_type != None and st_location != None:        
            content = job.objects.filter(Q(role__icontains=st_tc) | Q(company_name__icontains=st_tc), 
            job_location__icontains=st_location, category__icontains=st_type)

            # c1 =  job.objects.filter(role__icontains=st_tc)  
            # c2 =  job.objects.filter(company_name__icontains=st_tc)  
            # c3 =  job.objects.filter(job_location__icontains=st_location)  
            # c4 = job.objects.filter(category__icontains=st_type)
            # content = c1.union(c2, c3, c4)

            if len(content) == 0:
                messages.warning(request, 'No search result found. Please make sure that all words are spelled correctly')
            paginator = Paginator(content, 100, orphans=1)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            total_jobs = content.count()
    return render(request, 'job/searchresult.html', {'page_obj': page_obj, 'total_jobs':total_jobs, 'st_tc': st_tc})


# Filter jobs by batch
def filter_job_by_batch(request):
    if request.method == "GET":
        st=request.GET.get('batch')
        if st != None:
            content = {}
            content['data'] = job.objects.filter(yop__icontains=st)
            content['total_jobs'] = job.objects.filter(yop__icontains=st).count()
            content['st'] = st
    return render(request, 'job/filterjob.html',content)

# Filter jobs by location
def filter_job_by_location(request):
    if request.method == "GET":
        st=request.GET.get('joblocation')
        if st != None:
            content = {}
            content['data'] = job.objects.filter(job_location__icontains=st)
            content['total_jobs'] = job.objects.filter(job_location__icontains=st).count()
            content['st'] = st
    return render(request, 'job/filterjob.html',content)

# Filter jobs by degree
def filter_job_by_degree(request):
    if request.method == "GET":
        st=request.GET.get('degree')
        if st != None:
            content = {}
            content['data'] = job.objects.filter(qualification__icontains=st)
            content['total_jobs'] = job.objects.filter(qualification__icontains=st).count()
            content['st'] = st
    return render(request, 'job/filterjob.html',content)

# Sort jobs by date
def sort_job_by_date(request):
    content = {}
    content['data'] = job.jb_manager.sort_by_date()
    content['total_jobs'] = job.jb_manager.sort_by_date().count()
    return render(request, 'job/filterjob.html',content)

# About Jobportal
def about_page(request):
    return render(request, 'about.html', 
    {
        'total_users': User.objects.count(), 
        'total_jobs': job.objects.count(), 
        'companies': job.objects.order_by('company_name').values('company_name').distinct().count(),
        'total_vacancies' : job.objects.aggregate(Sum('vacancies'))['vacancies__sum']
    })

# Contact page for Jobportal
def contact_page(request):
    # user = request.user.username
    user = request.user
    x = uuid.uuid4()
    if request.method == 'POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
            j2 = fm.save(commit=False)
            if request.user.is_authenticated:
                j2.user_name = user
            else:
                # num = random.randint(0, 9999)
                Current_date = datetime.now().date()  
                Current_time = datetime.now().time()
                # j2.user_name = User.objects.create(username="Guest_"+str(Current_date)+"_"+str(Current_time), is_active=0)
                j2.user_name = User.objects.create(username="Guest_"+str(x), is_active=0)
            j2.save() 
            messages.success(request, "Your feedback has been successfully received. We'll get back to you soon")
            return redirect('index_page')
        else:
            for key, error in list(fm.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                messages.error(request, error) 

    else:
        if request.user.is_authenticated:
            fm = ContactForm(instance=Contact, initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email_id': request.user.email,
                'subject':"",
                'message':"",
            }) 
        else:
            fm = ContactForm()
    return render(request, 'contact.html', {'form':fm }) 

# Feedback Responses from contact
@login_required(login_url="handle_login")
def feedback_page(request):
    if request.user.is_authenticated and request.user.is_superuser:
        content = Contact.objects.all().order_by('-post_date')
        paginator = Paginator(content, 10, orphans=1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # print(content.values_list('user_name'))
        # if request.user.is_authenticated and request.user.is_superuser == True:
        #     users = User.objects.all()
        #     # users = content.values_list('user_name').filter(user_name= users1.get('username'))
        #     print(users)
        # else:
        #     users = None

        return render(request, 'feedback.html', {
            'page_obj': page_obj, 
            "total_feebacks": Contact.objects.count(),
            # "users": users
        })
    else:
        return render(request, 'error.html')