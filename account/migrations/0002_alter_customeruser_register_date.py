# Generated by Django 5.0.6 on 2024-05-14 13:30

import datetime
import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='register_date',
            field=django_jalali.db.models.jDateField(default=datetime.date(2024, 5, 14), verbose_name='تاریخ ثبت نام'),
        ),
    ]
