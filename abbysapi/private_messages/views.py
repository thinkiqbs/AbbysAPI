from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .serializers import ChatMessageSerializer
from .models import ChatMessage
from .serializers import MessageSerializer, SenderSerializer
from .models import Sender, Message
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics
from .models import Sender
from .serializers import MyUserSerializer, SenderSerializer
from accounts.models import MyUser


class SenderListCreateView(generics.ListCreateAPIView):
    queryset = Sender.objects.all()
    serializer_class = SenderSerializer


class SenderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sender.objects.all()
    serializer_class = SenderSerializer


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        sender_email = request.data.get('sender_email')
        recipient = request.data.get('recipient')
        message_text = request.data.get('message_text')

        # Retrieve a valid Sender instance using the sender_name field
        sender = Sender.objects.filter(name__email=sender_email).first()

        # If the Sender instance does not exist, create a new one
        if not sender:
            sender = Sender.objects.create(name=request.user)

        # Set the sender field of the Message instance to the retrieved or created Sender instance
        message = Message(sender=sender, recipient=recipient,
                          message_text=message_text)
        message.save()

        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class RetrieveMyUserView(generics.RetrieveAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        email = self.request.query_params.get('email')
        if email is None:
            raise Http404

        try:
            instance = self.get_queryset().get(email=email)
        except MyUser.DoesNotExist:
            raise Http404

        return instance


# views.py


class ChatMessageList(generics.ListAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['conversation_id', 'sender_id','receiver_id']

    def get_queryset(self):
        queryset = ChatMessage.objects.all()
        sender_email = self.request.query_params.get('sender_email', None)
        if sender_email is not None:
            queryset = queryset.filter(sender_id__icontains=sender_email)
        return queryset


class ChatMessageListCreateView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer


class ChatMessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ChatMessage
from .serializers import ChatMessageSerializer


class ChatMessageList(APIView):
    def get(self, request):
        chat_messages = ChatMessage.objects.all()
        serializer = ChatMessageSerializer(chat_messages, many=True)
        return Response(serializer.data)


class ChatMessageCreate(APIView):
    def post(self, request):
        serializer = ChatMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
