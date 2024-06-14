from rest_framework import serializers
from .models import Messages, Comments


class CommentsSerializer(serializers.ModelSerializer):
    post_title = serializers.ReadOnlyField(
        source="post.title"
    )  # Только для чтения, используется title сообщения

    class Meta:
        model = Comments
        fields = [
            "id",
            "post",
            "post_title",
            "content",
            "created_at",
        ]


class MessagesSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source="user.username"
    )  # Только для чтения, используется username
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Messages
        fields = ["id", "user", "title", "content", "created_at", "comments"]
