from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'description', 'amount', 'user']
        read_only_fields = ['user']  # Make the user field read-only

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Include fields you want to expose