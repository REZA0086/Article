# Generated by Django 5.0.6 on 2024-05-18 14:33

import datetime
import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='created_date',
            field=django_jalali.db.models.jDateField(default=datetime.date(2024, 5, 18), verbose_name='تاریخ ساخت'),
        ),
    ]