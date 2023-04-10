from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import QuestionListAPIView, QuestionCreateAPIView, QuestionDetailAPIView, AnswerCreateAPIView 


urlpatterns = [

    path('questions/', QuestionListAPIView.as_view(), name='question_list'),
    path('questions/create/', QuestionCreateAPIView.as_view(), name='question_create'),
    path('questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='question_detail'),
    path('questions/<int:pk>/answer/', AnswerCreateAPIView.as_view(), name='answer_create'),
    # path('messages/', ListMessagesView.as_view(), name='list_messages'),
    # path('messages/create/', CreateMessageView.as_view(), name='create_message'),
]
