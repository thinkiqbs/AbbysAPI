from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from .models import  Question, Answer
from .serializers import  QuestionSerializer, AnswerSerializer
from accounts.models import MyUser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status





class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer






class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class QuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerCreateAPIView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        question = get_object_or_404(Question, pk=self.kwargs['pk'])
        return Answer.objects.filter(question=question)

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, question=question)






# class ListMessagesView(generics.ListAPIView):
#     serializer_class = MessageSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         return Message.objects.filter(recipient=user)

# class CreateMessageView(generics.CreateAPIView):
#     serializer_class = MessageSerializer
#     # permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         sender = self.request.user
#         recipient_email = self.request.data.get('recipient')
#         recipient = MyUser.objects.get(email=recipient_email)
#         serializer.save(sender=sender, recipient=recipient)
