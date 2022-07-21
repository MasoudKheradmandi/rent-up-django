# Generated by Django 4.0.6 on 2022-07-20 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0023_alter_aparteman_image_alter_vilae_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=250)),
                ('Email_address', models.EmailField(max_length=254)),
                ('message', models.TextField(unique_for_date=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('Aparteman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.aparteman')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
