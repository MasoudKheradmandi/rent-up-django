# Generated by Django 4.0.5 on 2022-07-12 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aparteman',
            old_name='tabage',
            new_name='tabaghe',
        ),
        migrations.RemoveField(
            model_name='aparteman',
            name='map_1',
        ),
    ]
