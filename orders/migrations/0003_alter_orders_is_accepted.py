# Generated by Django 4.1.1 on 2022-09-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orders_pin_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='is_accepted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
