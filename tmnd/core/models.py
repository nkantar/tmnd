from django.conf import settings
from django.db.models import CASCADE, DateTimeField, ForeignKey, Model


class TimestampedModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(TimestampedModel):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
