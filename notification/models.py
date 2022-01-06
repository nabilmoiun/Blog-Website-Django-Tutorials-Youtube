from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from user_profile.models import User


class Notificaiton(models.Model):
    NOTIFICATION_TYPES = ("Blog", "Like", "Follow")

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.BigIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(
        User,
        related_name='user_notifications',
        on_delete=models.CASCADE
    )
    text = models.CharField(max_length=150)
    is_seen = models.BooleanField(default=False)
    notification_types = models.CharField(
        max_length=20,
        choices=list(zip(NOTIFICATION_TYPES, NOTIFICATION_TYPES))
    )
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
