from .serializers import MyUserSerializer
from .models import MyUser
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class CreateMessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Extract the recipient data from the request data
        recipient_data = request.data.get('recipient')

        # If recipient data is not provided, return a validation error
        if not recipient_data:
            return Response({'recipient': 'This field is required.'}, status=HTTP_400_BAD_REQUEST)

        # Create a new MyUser object for the recipient if it does not already exist
        recipient, created = MyUser.objects.get_or_create(**recipient_data)

        # Set the recipient field in the request data
        request.data['recipient'] = recipient.pk

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Set the sender to the current user
            serializer.save(sender=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class RetrieveMyUserView(generics.RetrieveAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'email'

    def get(self, request, *args, **kwargs):
        email = request.query_params.get('email')
        if email is None:
            return Response(status=HTTP_404_NOT_FOUND)

        try:
            instance = self.get_queryset().get(email=email)
        except MyUser.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
