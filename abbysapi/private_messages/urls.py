from django.urls import path
from .views import MessageList
from .views import CreateMessageView
from .views import RetrieveMyUserView

urlpatterns = [
    path('messages/', MessageList.as_view(), name='message-list'),
    path('messages/create/', CreateMessageView.as_view(), name='create_message'),
    path('users/<int:pk>/', RetrieveMyUserView.as_view(), name='retrieve_myuser'),
     path('users/', RetrieveMyUserView.as_view(), name='retrieve_myuser'),
]





