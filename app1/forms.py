from django import forms
from .models import job, Contact
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from autoslug import AutoSlugField

yop_ch =[
    ('Any Batch','Any Batch'),
    ('2020','2020'),
    ('2021','2021'),
    ('2022','2022'),
    ('2023','2023')
]

class jobapply(forms.ModelForm):
    
    last_date = forms.DateField(label='Last Date to Apply (yyyy-mm-dd)', widget=forms.NumberInput(attrs={'type': 'date'}))
    #yop = forms.ChoiceField(label='Year of Passing', choices=yop_ch, widget=forms.RadioSelect())
    vacancies = forms.IntegerField(label='Vacancies', widget=forms.NumberInput())
    drive_location = forms.CharField(label='Drive Location', widget=forms.Textarea(attrs={"rows":"3"}))
    #yop = forms.MultipleChoiceField(choices=yop_ch, widget=forms.CheckboxSelectMultiple())
    #yop = forms.MultipleChoiceField(choices=yop_ch)
    #yop = forms.MultipleChoiceField(choices=yop_ch, widget=forms.TextInput(attrs={'type': 'checkbox'}))
    #yop = forms.MultipleChoiceField(choices=yop_ch, widget=forms.SelectMultiple())
    #yop = forms.ModelMultipleChoiceField(queryset=job.objects.get('yop'), widget=forms.CheckboxSelectMultiple())

    required_css_class = 'required'

    class Meta:
        model = job

        #custom label for model form field
        labels = {
            'job_id': 'Job ID',
            'role' :'Job Role',
            'company_name': 'Company Name',
            'company_site': 'Company Website',
            'category': 'Job Category',
            'salary': 'Salary(LPA)',
            'yop' : 'Year of Passing',
            'job_location': 'Job Location',
            'qualification': 'Qualification',
            'experience': 'Experience(In years)',
            'venue_details': 'Venue Details',
            'apply_link': 'Apply Link',
            'published_date': 'Published On',
            'last_modified': 'Last Modified On', 
            'publisher_name': 'Posted By',
            'updated_by': 'Updated By'
        }

        fields = '__all__'
        #exclude = ['last_modified']
        exclude = ['venue_details','publisher_name','updated_by','favourites','views']
        localized_fields = ('__all__')


        #Overriding the default fields
        widgets = {
            #'body': forms.Textarea(attrs={'rows': 3}),
        }

class EditUserProfileForm(UserChangeForm):
    password = None
    slug = AutoSlugField(populate_from='User.username', max_length=200, unique=True, null=True, editable=False)
    required_css_class = 'required'

    class Meta:
        model = User
        labels = {
        }

        # fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
        # exclude = ['']

class EditAdminProfileForm(UserChangeForm):
    password = None
    slug = AutoSlugField(populate_from='User.username', max_length=200, unique=True, null=True, editable=False)
    required_css_class = 'required'

    class Meta:
        model = User
        labels = {
        }

        fields = '__all__'
        #fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login','is_active']
        # exclude = ['']
       
class ContactForm(forms.ModelForm):
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={"rows":"7", 'placeholder': 'Write your notes or questions here...'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    required_css_class = 'required'

    class Meta:
        model = Contact
        labels = {
            'fisrt_name': 'First Name',
            'last_name': 'Last Name',
            'email_id': 'Email',
            'subject': 'Subject',
            'post_date': 'Posted On',
        }
        fields = '__all__' 
        exclude = ['user_name']