# Generated by Django 4.0.4 on 2022-07-18 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_rename_image_aparteman_images_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vilae',
            name='parking',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
