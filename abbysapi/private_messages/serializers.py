
from rest_framework import serializers
from .models import Sender, Message
from accounts.models import MyUser

from rest_framework import serializers
from .models import Sender, Message,Recipient


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name']


class SenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sender
        fields = '__all__'


class RcipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'




class MessageSerializer(serializers.ModelSerializer):
    sender = SenderSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'message_text', 'created_at']



from rest_framework import serializers
from .models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'



from rest_framework import serializers
from .models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ('id', 'conversation_id', 'sender_id', 'receiver_id', 'participants', 'message', 'timestamp')


