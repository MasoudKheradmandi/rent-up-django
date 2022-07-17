# Generated by Django 4.0.5 on 2022-07-13 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_alter_aparteman_andaze_alter_aparteman_tabaghe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparteman',
            name='tabaghe',
            field=models.PositiveIntegerField(verbose_name='طبقه'),
        ),
        migrations.AlterField(
            model_name='aparteman',
            name='tedad_vahed_tabaghe',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='تعداد واحد در هر طبقه'),
        ),
        migrations.CreateModel(
            name='vilae',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titr', models.CharField(max_length=300, verbose_name='تیتر')),
                ('status_buy', models.CharField(choices=[('برای خرید', 'برای خرید'), ('برای اجاره', 'برای اجاره')], default='برای خرید', max_length=50, verbose_name='برای خرید/رهن و اجاره')),
                ('gheymat', models.BigIntegerField(default=0, verbose_name='قیمت')),
                ('gheymat_rahn', models.PositiveIntegerField(default=0, verbose_name='قیمت رهن')),
                ('gheymat_ejare', models.PositiveIntegerField(default=0, verbose_name='قیمت اجاره')),
                ('locations', models.TextField(verbose_name='ادرس ویلا')),
                ('sanad', models.CharField(choices=[('شش دانگ', 'شش دانگ'), ('مشاع', 'مشاع'), ('اصلاخات ارضی', 'اصلاحات ارضی')], default='شش دانگ', max_length=32, verbose_name='نوع سند')),
                ('andaze_zamin', models.PositiveSmallIntegerField(verbose_name='اندازه زمین')),
                ('andaze_bana', models.PositiveSmallIntegerField(verbose_name='اندازه بنا')),
                ('tedad_otagh', models.PositiveSmallIntegerField(verbose_name='تعداد اتاق')),
                ('tedad_dastshoe', models.PositiveSmallIntegerField(verbose_name='تعداد سرویس بهداشتی')),
                ('sal_sakht', models.CharField(choices=[('0-5', '0-5'), ('5-10', '5-10'), ('10-20', '10-20'), ('20+', '20+')], default='0-5', max_length=10)),
                ('ghabel_moaveze', models.BooleanField(default=False, verbose_name='قابل معاوضه؟')),
                ('tozihat_karbar', models.TextField(verbose_name='توضیحات کاربر')),
                ('tozihat_khososy', models.TextField(blank=True, null=True, verbose_name='توضیحات خصوصی')),
                ('map_1', models.TextField(blank=True, null=True, verbose_name='نقشه گوگل')),
                ('image', models.ImageField(upload_to='', verbose_name='عکس اصلی')),
                ('upload_time', models.DateField(default=django.utils.timezone.now, verbose_name='زمان ثبت')),
                ('vise', models.BooleanField(default=False, verbose_name='ویژه؟')),
                ('active', models.BooleanField(default=True, verbose_name='نمایش؟')),
                ('tahvie', models.BooleanField(default=False)),
                ('internet', models.BooleanField(default=False)),
                ('trass', models.BooleanField(default=False)),
                ('wifi', models.BooleanField(default=False)),
                ('bed', models.BooleanField(default=False)),
                ('micro', models.BooleanField(default=False)),
                ('balcony', models.BooleanField(default=False)),
                ('sahel', models.BooleanField(default=False)),
                ('system_garmayeshi', models.BooleanField(default=False)),
                ('sigary', models.BooleanField(default=False)),
                ('nevisande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'ویلا',
                'verbose_name_plural': 'ویلاها',
                'ordering': ['-upload_time'],
            },
        ),
    ]
