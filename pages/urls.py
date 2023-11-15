from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('accounts/<int:pk>/', views.UserDetailView.as_view(), name='profile'),
    path('accounts/<int:pk>/update/',
         views.UserUpdateView.as_view(), name='update_profile'),
    path('accounts/<int:pk>/inbox/', include('inboxes.urls')),
]
