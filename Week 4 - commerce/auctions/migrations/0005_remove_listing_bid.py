# Generated by Django 5.1.3 on 2025-01-21 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='bid',
        ),
    ]
