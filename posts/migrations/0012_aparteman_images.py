# Generated by Django 4.0.5 on 2022-07-18 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_zamin'),
    ]

    operations = [
        migrations.CreateModel(
            name='aparteman_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.aparteman')),
            ],
        ),
    ]
