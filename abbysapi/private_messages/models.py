from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from accounts.models import MyUser


# class Message(models.Model):
#     sender = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='sent_messages')
#     recipient = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='received_messages')
#     text = models.TextField()
#     timestamp = models.DateTimeField()


class Message(models.Model):
    sender = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='received_messages')
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"From {self.sender.email} to {self.recipient.email}: {self.message_text[:20]}..."
