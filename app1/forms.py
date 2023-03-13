from django import forms
from .models import job

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
            'last_modified': 'Last Modified On' 
        }

        fields = '__all__'
        #exclude = ['last_modified']
        exclude = ['venue_details']
        localized_fields = ('__all__')


        #Overriding the default fields
        widgets = {
            #'body': forms.Textarea(attrs={'rows': 3}),
        }

