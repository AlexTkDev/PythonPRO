from django.db import models


class Member(models.Model):
    save_text = models.TextField()

    def __str__(self):
        return self.save_text
