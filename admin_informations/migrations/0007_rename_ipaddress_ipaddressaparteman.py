# Generated by Django 4.0.6 on 2022-07-21 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_informations', '0006_ipaddress'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IPAddress',
            new_name='IPAddressAparteman',
        ),
    ]
