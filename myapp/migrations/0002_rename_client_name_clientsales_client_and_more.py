# Generated by Django 5.1 on 2024-09-01 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientsales',
            old_name='client_name',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='clientsales',
            old_name='shop_name',
            new_name='shop',
        ),
    ]
