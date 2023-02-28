from django.urls import path

from .views import (
    ThreadListCreateView,
    ThreadRetrieveDestroyView,
    MessageListCreateView,
    MessageRetrieveUpdateDestroyView,
    MarkMessageReadView,
    UnreadMassageCountView
)

app_name = 'threads'

urlpatterns = [
    path('', ThreadListCreateView.as_view(), name='thread_list_create'),
    path('<int:pk>/', ThreadRetrieveDestroyView.as_view(), name='thread_retrive_destroy'),
    path('<int:thread_id>/messages/', MessageListCreateView.as_view(), name='message_list_create'),
    path('<int:thread_id>/messages/<int:pk>/', MessageRetrieveUpdateDestroyView.as_view(), name='message_retrieve_destroy'),
    path('<int:thread_id>/mark_read/', MarkMessageReadView.as_view(), name='mark-read-messages'),
    path('<int:thread_id>/unread_count/', UnreadMassageCountView.as_view(), name='unread-count-message')
]