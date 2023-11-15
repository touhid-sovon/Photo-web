from django.urls import path
from . import views


urlpatterns = [
    path('', views.InboxListView.as_view(), name='inbox'),
    path('<int:inbox_pk>/', views.InboxDetailView.as_view(), name='inbox_detail'),
]
