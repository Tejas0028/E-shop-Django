from django.db import models

# Create your models here.

class HoneypotAttempt(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attempt from {self.ip_address} at {self.timestamp}"
