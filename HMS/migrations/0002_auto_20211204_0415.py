# Generated by Django 3.2.9 on 2021-12-04 04:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HMS', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customers',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='customers_id',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='customers_id',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='customers_id',
            new_name='customer_id',
        ),
    ]
