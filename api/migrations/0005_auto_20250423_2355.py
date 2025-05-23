# Generated by Django 3.2.25 on 2025-04-23 21:55

from django.db import migrations, models
import uuid

def populate_tokens(apps, schema_editor):
    Transaction = apps.get_model('api', 'Transaction')
    for transaction in Transaction.objects.all():
        try:
            # Assign a unique token to each transaction
            transaction.token = uuid.uuid4()
            transaction.save(update_fields=['token'])
        except Exception as e:
            print(f"Skipping transaction with ID {transaction.id} due to error: {e}")

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_transaction_amount'),  # Replace with the correct previous migration
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='transaction',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.RunPython(populate_tokens),  # Populate tokens for existing rows
        migrations.AlterField(
            model_name='transaction',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
