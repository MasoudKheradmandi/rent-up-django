# Generated by Django 4.0.6 on 2022-07-20 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_alter_aparteman_image_alter_vilae_image'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='CommentAparteman',
        ),
    ]
