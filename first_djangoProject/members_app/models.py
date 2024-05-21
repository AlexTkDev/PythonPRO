from django.db import models


class Member(models.Model):
    save_text = models.TextField()

    class Meta:
        verbose_name = 'введённый текст'
        verbose_name_plural = "всё что мы ввели:"

    def __str__(self):
        return self.save_text
