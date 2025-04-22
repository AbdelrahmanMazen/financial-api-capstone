from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, blank=True, null=True)  # Add token field

    def __str__(self):
        return f"{self.description} - {self.amount}"