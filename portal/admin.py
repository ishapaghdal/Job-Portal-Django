from django.contrib import admin
from .models import JobPost

class JobPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'salary_range']
    search_fields = ['title', 'company__name', 'tags__name']

admin.site.register(JobPost, JobPostAdmin)
