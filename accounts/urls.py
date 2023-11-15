from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout_page/',
         TemplateView.as_view(template_name='registration/logout.html'), name='logout_page'),
    path('<int:pk>/', views.ProfileDetailView.as_view(), name='account'),
]
