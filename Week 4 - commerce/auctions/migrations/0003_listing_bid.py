# Generated by Django 5.1.3 on 2025-01-17 21:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bid',
            field=models.ManyToManyField(blank=True, null=True, related_name='listingBid', to=settings.AUTH_USER_MODEL),
        ),
    ]
