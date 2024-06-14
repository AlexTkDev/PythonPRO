from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}: {self.user}"


class Comments(models.Model):
    post = models.ForeignKey(
        Messages, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post}: {self.content}"
