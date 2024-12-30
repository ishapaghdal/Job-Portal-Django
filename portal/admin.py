from django.contrib import admin
from .models import JobPost

class JobPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'salary_range']
    search_fields = ['title', 'company__name', 'tags__name']
    # filter_horizontal = ('tags',)  # This will add a multi-select box for tags

admin.site.register(JobPost, JobPostAdmin)
# admin.site.register(Tag)
