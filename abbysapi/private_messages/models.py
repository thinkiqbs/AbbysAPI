import datetime
from django.db import models
from accounts.models import MyUser
from forum.models import Question

class Sender(models.Model):
    sender = models.OneToOneField(MyUser, on_delete=models.CASCADE)

class Recipient(models.Model):
    recipient = models.OneToOneField(Question, on_delete=models.CASCADE)

class Message(models.Model):
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    message_subject = models.CharField(max_length=255)
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)





class ChatMessage(models.Model):

    conversation_id = models.CharField(max_length=100)
    sender_id = models.CharField(max_length=100)
    receiver_id = models.CharField(max_length=100)
    participants = models.JSONField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



