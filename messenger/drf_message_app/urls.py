from django.urls import path
from .views import (
    UserMessagesView,
    MessageCommentsView,
    MessageDetailView,
    MessageCreateView,
    CommentCreateView,
    CommentDetailView,
)

urlpatterns = [
    path("messages/", UserMessagesView.as_view(), name="user-messages"),
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="message-detail"),
    path(
        "messages/<int:message_id>/comments/",
        MessageCommentsView.as_view(),
        name="message-comments",
    ),
    path("messages/create/", MessageCreateView.as_view(), name="message-create"),
    path(
        "messages/<int:message_id>/comments/create/",
        CommentCreateView.as_view(),
        name="comment-create",
    ),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
]
