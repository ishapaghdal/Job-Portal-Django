from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CompanyForm, JobPostForm
from .models import Company, JobPost
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

# Signup
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('register_company') 
    else:
        form = UserCreationForm()
    return render(request, 'portal/signup.html', {'form': form})

# Login 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if not hasattr(user, 'company'):
                return redirect('register_company') 
            
            return redirect('job_list') 
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'portal/login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

#login
@login_required
def register_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            return redirect('job_list')
    else:
        form = CompanyForm()
    return render(request, 'portal/register_company.html', {'form': form})

#create job
@login_required
def create_job_post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.company
            job.save()
            return redirect('job_list')
    else:
        form = JobPostForm()
    return render(request, 'portal/create_job_post.html', {'form': form})

#list job
@login_required
def job_list(request):
    jobs = JobPost.objects.filter()
    paginator = Paginator(jobs, 2)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'portal/job_list.html', {'page_obj': page_obj})

#edit job
@login_required
def edit_job_post(request, pk):
    job = get_object_or_404(JobPost, pk=pk, company=request.user.company)
    
    if request.method == 'POST':
        form = JobPostForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobPostForm(instance=job)

    return render(request, 'portal/edit_job_post.html', {'form': form})

#edit company
@login_required
def edit_company(request):
    company = request.user.company
    
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = CompanyForm(instance=company)

    return render(request, 'portal/edit_company.html', {'form': form})

#delete job
@login_required
def delete_job_post(request, pk):
    job = JobPost.objects.get(pk=pk, company=request.user.company)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request, 'portal/delete_job_post.html', {'job': job})
