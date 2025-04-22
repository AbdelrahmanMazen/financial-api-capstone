from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .models import Transaction, User as CustomUser
from .serializers import TransactionSerializer, UserSerializer
import uuid

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]  # Allow unauthenticated access

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class TransactionListCreateView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]  # Require authentication

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            raise ValidationError({"user": "Authentication is required to create a transaction."})

@login_required
def home(request):
    if request.method == "POST":
        transaction_id = request.POST.get("id")
        description = request.POST.get("description")
        amount = request.POST.get("amount")

        try:
            # Check if the ID already exists
            if Transaction.objects.filter(id=transaction_id).exists():
                raise IntegrityError(f"A transaction with ID {transaction_id} already exists.")

            # Save the transaction
            Transaction.objects.create(
                id=transaction_id,
                description=description,
                amount=amount,
                user=request.user
            )
            return redirect('home')

        except IntegrityError as e:
            # Render the form with an error message
            return render(request, 'index.html', {"error": str(e)})

    return render(request, 'index.html')

def transaction_history(request):
    transactions = Transaction.objects.all()  # Fetch all transactions
    return render(request, 'transaction_history.html', {"transactions": transactions})

def transaction_detail(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    return render(request, 'transaction_detail.html', {'transaction': transaction})

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}