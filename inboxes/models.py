from django.db import models
from accounts.models import CustomUserModel

# Create your models here.


class Inbox(models.Model):
    sender = models.ForeignKey(
        CustomUserModel, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(
        CustomUserModel, on_delete=models.CASCADE, related_name='received_messages')
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    message_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.body
