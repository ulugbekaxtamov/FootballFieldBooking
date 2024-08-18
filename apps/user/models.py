import uuid as uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    class Meta:
        ordering = ('-id',)

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='user/images/', null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)

    def __str__(self):
        return f"{self.id} - {self.username}"
