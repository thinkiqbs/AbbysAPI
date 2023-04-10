from rest_framework import serializers
from .models import  Message
from accounts.models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'user_type', 'date_of_birth', 'nickname']

        
class MessageSerializer(serializers.ModelSerializer):
    sender = MyUserSerializer(read_only=True)
    recipient = MyUserSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'message_text', 'created_at']
