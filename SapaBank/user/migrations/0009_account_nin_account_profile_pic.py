# Generated by Django 5.1.3 on 2024-12-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_transaction_transaction_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='NIN',
            field=models.CharField(blank=True, default=0, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='profile_pic',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
