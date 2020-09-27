from django.db import models
from django.contrib.auth.models import User


class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="diary", null=True)
    message = models.TextField()
    pub_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[0:15] + " ..."
