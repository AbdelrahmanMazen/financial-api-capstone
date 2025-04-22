from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Transaction
from django.contrib.auth.models import User

class TransactionAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.transaction_data = {
            'transaction_date': '2023-01-01',
            'description': 'Test Transaction',
            'amount': 100.00,
            'user_id': self.user.id
        }
        self.transaction = Transaction.objects.create(**self.transaction_data)

    def test_create_transaction(self):
        response = self.client.post(reverse('transaction-list'), self.transaction_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 2)

    def test_get_transaction(self):
        response = self.client.get(reverse('transaction-detail', args=[self.transaction.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], self.transaction.description)

    def test_update_transaction(self):
        updated_data = {'description': 'Updated Transaction'}
        response = self.client.patch(reverse('transaction-detail', args=[self.transaction.id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.transaction.refresh_from_db()
        self.assertEqual(self.transaction.description, 'Updated Transaction')

    def test_delete_transaction(self):
        response = self.client.delete(reverse('transaction-detail', args=[self.transaction.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Transaction.objects.count(), 0)