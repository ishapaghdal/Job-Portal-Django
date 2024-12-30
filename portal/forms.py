from django import forms
from .models import Company, JobPost

class CompanyForm(forms.ModelForm):
    name = forms.CharField(label='Company Name')
    address = forms.CharField(label='Company Address')
    contact_number = forms.CharField(label='Contact Number')
    class Meta:
        model = Company
        fields = ['name', 'address', 'contact_number']

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'location', 'salary_range', 'tags']
    # tags = forms.ModelMultipleChoiceField(
    #     queryset=Tag.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False
    # )
