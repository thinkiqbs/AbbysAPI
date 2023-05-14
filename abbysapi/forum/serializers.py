from rest_framework import serializers
from .models import  Question, Answer
from accounts.models import MyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'username', 'email', 'user_type', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Question
        fields = ['id', 'user','title', 'question_text', 'created_at']

class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    question = QuestionSerializer()
    class Meta:
        model = Answer
        fields = ['id', 'user', 'question', 'answer_text', 'created_at']


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'user_type', 'date_of_birth', 'nickname')
        read_only_fields = ('id', 'email')

# class MessageSerializer(serializers.ModelSerializer):
#     sender = MyUserSerializer(source='sender.email')
#     # recipient = MyUserSerializer(source='recipient.email')

#     class Meta:
#         model = Message
#         fields = ['sender', 'recipient', 'message_text', 'created_at']
