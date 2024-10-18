from django.db import models
import uuid

class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    account_name = models.CharField(max_length=255)
    app_secret_token = models.UUIDField(default=uuid.uuid4, editable=False)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.account_name