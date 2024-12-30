from django.urls import path
from . import views

urlpatterns = [
    path('register_company/', views.register_company, name='register_company'),
    path('edit_company/', views.edit_company, name='edit_company'),
    path('create_job_post/', views.create_job_post, name='create_job_post'),
    path('job_list/', views.job_list, name='job_list'),
    path('edit_job_post/<int:pk>/', views.edit_job_post, name='edit_job_post'),
    path('delete_job_post/<int:pk>/', views.delete_job_post, name='delete_job_post'),
]
