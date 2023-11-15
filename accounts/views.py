from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .models import CustomUserModel

# Create your views here.


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')


class ProfileDetailView(DetailView):
    model = CustomUserModel
    template_name = 'profile_detail.html'
    context_object_name = 'user'
