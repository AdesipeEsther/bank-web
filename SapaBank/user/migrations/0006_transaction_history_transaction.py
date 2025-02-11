# Generated by Django 5.1.3 on 2024-11-28 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_delete_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.account')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField(default=0)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receiver', to='user.account')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sender', to='user.account')),
                ('transaction_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='user.transaction_history')),
            ],
        ),
    ]
