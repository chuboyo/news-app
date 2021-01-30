from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
   form_class = CustomUserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'registration/signup.html'
