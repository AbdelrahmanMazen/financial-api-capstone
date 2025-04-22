from django.urls import path
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Transaction
from .views import transaction_history

def transaction_history(request):
    transactions = Transaction.objects.all()
    paginator = Paginator(transactions, 10)  # Show 10 transactions per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'transaction_history.html', {"page_obj": page_obj})

urlpatterns = [
    path('transactions/', transaction_history, name='transaction_history'),
]