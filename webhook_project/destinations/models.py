from django.db import models
from accounts.models import Account


class Destination(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="destinations"
    )
    url = models.URLField()
    http_method = models.CharField(
        max_length=10, choices=[("GET", "GET"), ("POST", "POST"), ("PUT", "PUT")]
    )
    headers = models.JSONField()

    def __str__(self):
        return f"{self.account.account_name} - {self.url}"


"""
Ex for headers:
{
“APP_ID”: "",
“APP_SECTET”: “”,
“ACTION”: “user.update”,
“Content-Type”: “application/JSON”,
“Accept”: “*”
}
"""
