import uuid
from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Random token

    def __str__(self):
        return f"{self.description} - {self.amount}"