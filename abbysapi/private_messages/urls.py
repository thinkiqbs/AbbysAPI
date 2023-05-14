from django.urls import path
from .views import (
    SenderListCreateView,
    SenderRetrieveUpdateDestroyView,
    MessageListCreateView,
    MessageRetrieveUpdateDestroyView,
    RetrieveMyUserView,
)

from .views import ChatMessageList
from django.urls import path
from .views import ChatMessageListCreateView, ChatMessageRetrieveUpdateDestroyView
from django.urls import path
from .views import ChatMessageList, ChatMessageCreate

urlpatterns = [
    path('senders/', SenderListCreateView.as_view(), name='sender-list-create'),
    path('senders/<int:pk>/', SenderRetrieveUpdateDestroyView.as_view(), name='sender-retrieve-update-destroy'),
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDestroyView.as_view(), name='message-retrieve-update-destroy'),
    path('users/', RetrieveMyUserView.as_view(), name='user-detail'),
    path('messagesChat/', ChatMessageList.as_view(), name='message-list'),
    path('messagesChat/<int:pk>/', ChatMessageList.as_view(), name='message-list'),
    path('messagesChatCreate/', ChatMessageListCreateView.as_view(), name='chat-message-list-create'),
    path('messagesChatDelete/<int:pk>/', ChatMessageRetrieveUpdateDestroyView.as_view(), name='chat-message-retrieve-update-destroy'),
    path('messagesChat/<str:email>/', ChatMessageList.as_view(), name='message-list-by-email'),
    path('chat_messages/', ChatMessageList.as_view(), name='chat_message_list'),
    path('chat_messages/create/', ChatMessageCreate.as_view(), name='chat_message_create'),
]






