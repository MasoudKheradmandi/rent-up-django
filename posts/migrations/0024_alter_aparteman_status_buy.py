# Generated by Django 4.0.4 on 2022-07-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_alter_aparteman_image_alter_vilae_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparteman',
            name='status_buy',
            field=models.CharField(choices=[('برای خرید', 'برای خرید'), ('برای اجاره', 'برای اجاره')], default='برای خرید', max_length=50, verbose_name='برای خرید/رهن و اجاره'),
        ),
    ]
