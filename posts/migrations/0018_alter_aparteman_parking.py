# Generated by Django 4.0.5 on 2022-07-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_alter_aparteman_image_alter_aparteman_parking_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparteman',
            name='parking',
            field=models.IntegerField(),
        ),
    ]
