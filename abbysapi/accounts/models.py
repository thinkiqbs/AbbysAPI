from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser

class MyUser(EmailAbstractUser):
    USER_TYPE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=20, default='student')
    date_of_birth = models.DateField('Date of birth', null=True, blank=True)
    nickname = models.CharField(max_length=50, null=True, blank=True)

    objects = EmailUserManager()


