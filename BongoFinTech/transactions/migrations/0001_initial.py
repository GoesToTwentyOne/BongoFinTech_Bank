# Generated by Django 4.2.4 on 2023-08-20 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTransactionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('balance_after_transaction', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('transaction_type', models.IntegerField(choices=[('DEPOSIT', 'Deposit'), ('WITHDRAW', 'Withdraw'), ('LOAN', 'Loan'), ('LOAN_PAID', 'Loan_Paid')], null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('loan_approved', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_transactions', to='accounts.userbankaccountmodel')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
