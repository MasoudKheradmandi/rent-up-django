# Generated by Django 4.0.5 on 2022-07-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_remove_vilae_parking_alter_aparteman_parking'),
    ]

    operations = [
        migrations.AddField(
            model_name='vilae',
            name='parking',
            field=models.CharField(max_length=2, null=True),
        ),
    ]