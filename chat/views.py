from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Thread, Message
from .serializer import ThreadSerializer, MessageSerializer, MessageCreateSerializer

class ThreadListCreateView(generics.ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Thread.objects.filter(participants=self.request.user)
    
    def create(self, request, *args, **kwargs):
        participants = request.data.get('participants')
        if not participants or len(participants) != 2:
            return Response({'message': 'Thread can have only 2 users'}, status=status.HTTP_400_BAD_REQUEST)
        user1, user2 = participants
        thread = Thread.objects.filter(participants=user1).filter(participants=user2).first()
        if thread:
            serializer = self.get_serializer(thread)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class ThreadRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        thread = get_object_or_404(Thread, id=self.kwargs['pk'], participants=self.request.user)
        return thread
    

class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        thread_id = self.kwargs['thread_id']
        return Message.objects.filter(thread=thread_id)
    
    def post(self, request, thread_id):
        request.data['thread'] = thread_id
        serializer = MessageCreateSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.save(sender=request.user)
            message_serializer = MessageSerializer(message).data
            return Response(message_serializer, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        thread_id = self.kwargs['thread_id']
        message_id = self.kwargs['pk']
        return get_object_or_404(Message, id=message_id, thread=thread_id)
    
class MarkMessageReadView(generics.UpdateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        thread_id = self.kwargs['thread_id']
        return Message.objects.filter(thread=thread_id, is_read=False)
    
    def partial_update(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.update(is_read=True)
        return Response(status=status.HTTP_200_OK)

class UnreadMassageCountView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, thread_id):
        count = Message.objects.filter(thread__id=thread_id, is_read=False).exclude(sender=self.request.user).count()
        return Response({'count': count}, status=status.HTTP_200_OK)
