# Generated by Django 4.0.5 on 2022-07-15 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0010_vilae_parking'),
    ]

    operations = [
        migrations.CreateModel(
            name='zamin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titr', models.CharField(max_length=150, verbose_name='تیتر')),
                ('gheymat', models.PositiveIntegerField(verbose_name='قیمت')),
                ('andaze', models.PositiveSmallIntegerField(verbose_name=' اندازه')),
                ('noe_zamin', models.CharField(choices=[('تفریحی توریستی', 'تفریحی توریستی'), ('باغ', 'باغ'), ('مسکونی', 'مسکونی')], default='مسکونی', max_length=30, verbose_name='نوع زمین')),
                ('locations', models.TextField(verbose_name='ادرس زمین')),
                ('sanad', models.CharField(choices=[('شش دانگ', 'شش دانگ'), ('مشاع', 'مشاع'), ('اصلاحات ارضی', 'اصلاحات ارضی')], default='شش دانگ', max_length=32, verbose_name='نوع سند')),
                ('ghabel_moaveze', models.BooleanField(default=False, verbose_name='قابل معاوضه؟')),
                ('tozihat_karbar', models.TextField(verbose_name='توضیحات کاربر')),
                ('tozihat_khososy', models.TextField(blank=True, null=True, verbose_name='توضیحات خصوصی')),
                ('image', models.ImageField(upload_to='', verbose_name='عکس اصلی')),
                ('upload_time', models.DateField(default=django.utils.timezone.now, verbose_name='زمان ثبت')),
                ('vise', models.BooleanField(default=False, verbose_name='ویژه؟')),
                ('active', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('nevisande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'زمین',
                'verbose_name_plural': 'زمین ها',
                'ordering': ['-upload_time'],
            },
        ),
    ]