# Generated by Django 3.2.9 on 2021-12-06 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0016_alter_roomstatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomstatus',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Expired', 'Expired')], default=0, max_length=20),
        ),
    ]
