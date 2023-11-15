from django.db import models
from accounts.models import CustomUserModel
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='post_image/')
    liked = models.ManyToManyField(
        CustomUserModel, related_name='liked_posts',)

    def total_likes_count(self):
        return self.liked.count()

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('detail_post', args=[str(self.id)])


class Comment(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    def total_comment_count(self):
        return self.body.count()

    def get_absolute_url(self):
        return reverse('detail_post', args=[str(self.post.id)])

    class Meta:
        ordering = ['-id']
