# Generated by Django 4.1.1 on 2022-09-22 05:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_address_customer_district_customer_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone_no',
            field=models.CharField(default=None, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
