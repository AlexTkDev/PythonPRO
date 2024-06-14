from rest_framework import generics, permissions
from .models import Messages, Comments
from .serializers import MessagesSerializer, CommentsSerializer


# Просмотр всех сообщений текущего пользователя
class UserMessagesView(generics.ListAPIView):
    serializer_class = MessagesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Получение всех сообщений принадлежащих текущему пользователю.
        """
        return Messages.objects.filter(user=self.request.user)


# Просмотр всех комментариев к сообщению
class MessageCommentsView(generics.ListAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Получение всех комментариев к конкретному сообщению,
        принадлежащему текущему пользователю.
        """
        message_id = self.kwargs["message_id"]
        return Comments.objects.filter(
            post__id=message_id, post__user=self.request.user
        )


# Просмотр, обновление и удаление конкретного сообщения текущего пользователя
class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessagesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Получение конкретного сообщения текущего пользователя по его идентификатору.
        """
        return Messages.objects.filter(user=self.request.user)


# Создание нового сообщения
class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessagesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Создание нового сообщения с привязкой к текущему пользователю.
        """
        serializer.save(user=self.request.user)


# Создание нового комментария для сообщения текущего пользователя
class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Создание нового комментария для определенного сообщения,
        принадлежащего текущему пользователю.
        """
        message = Messages.objects.get(
            pk=self.kwargs["message_id"], user=self.request.user
        )
        serializer.save(post=message)


# Просмотр, обновление и удаление конкретного комментария текущего пользователя
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Получение конкретного комментария, принадлежащего текущему пользователю.
        """
        return Comments.objects.filter(post__user=self.request.user)
