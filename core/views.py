from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .forms import JobForm
from .models import Job


# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('job_list')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'job_list.html', {'jobs': jobs})

@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'post_job.html', {'form': form})
