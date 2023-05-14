from django.db import models
from accounts.models import MyUser


class Question(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    # title = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



# class Message(models.Model):
#     sender = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='sent_messages')
#     recipient = models.EmailField()
#     message_text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return f"From {self.sender.email} to {self.recipient.email}: {self.message_text[:20]}..."


# # in forum/models.py
# class Message(models.Model):
#     sender = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='forum_messages_sent')
#     recipient = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='forum_messages_received')
#     text = models.TextField()
#     timestamp = models.DateTimeField()