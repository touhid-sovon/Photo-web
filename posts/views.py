from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    fields = ['description', 'image']
    success_url = reverse_lazy('post')

    def form_valid(self, form):
        # Set the user field to the logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail_post.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/update_post.html'
    fields = ['description']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('post')


def PostLikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    if post.liked.filter(id=request.user.id).exists():
        post.liked.remove(request.user)
    else:
        post.liked.add(request.user)

    return HttpResponseRedirect(reverse('detail_post', args=[str(pk)]))


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment/create_comment.html'
    fields = ['body']
    success_url = reverse_lazy('detail_post')

    def form_valid(self, form):
        # Retrieve the associated post based on post_id in the URL
        post_id = self.kwargs['pk']
        post = get_object_or_404(Post, id=post_id)

        # Set the comment's post field
        form.instance.post = post
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the post detail page
        return reverse('detail_post', args=[str(self.kwargs['pk'])])


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'comment/edit_comment.html'
    fields = ['body']


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment/delete_comment.html'

    def get_success_url(self):
        # Redirect back to the post detail page
        return reverse('detail_post', args=[str(self.object.post.pk)])
