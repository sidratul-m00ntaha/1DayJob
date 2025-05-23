from django import forms
from .models import Job
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'estimated_time', 'reward', 'category']

        