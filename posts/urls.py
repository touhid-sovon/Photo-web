from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post'),
    path('add_post/', views.PostCreateView.as_view(), name='create_post'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail_post'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update_post'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
    path('<int:pk>/like/', views.PostLikeView, name='like_post'),
    path('<int:pk>/comment/', views.CommentCreateView.as_view(),
         name='create_comment'),
    path('<int:pk>/comment/edit/',
         views.CommentUpdateView.as_view(), name='update_comment'),
    path('<int:pk>/comment/delete/',
         views.CommentDeleteView.as_view(), name='delete_comment'),

]
