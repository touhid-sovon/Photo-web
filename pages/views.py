from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, UpdateView
from accounts.models import CustomUserModel
from django.urls import reverse

# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class UserDetailView(DetailView):
    model = CustomUserModel
    template_name = 'profile.html'
    context_object_name = 'user'


class UserUpdateView(UpdateView):
    model = CustomUserModel
    template_name = 'edit_profile.html'
    fields = ['first_name', 'last_name', 'username', 'dob', 'profile_picture']

    def get_success_url(self):
        return reverse('profile', args=[str(self.kwargs['pk'])])
