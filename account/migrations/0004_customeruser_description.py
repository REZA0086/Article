# Generated by Django 5.0.6 on 2024-05-16 06:22

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customeruser_register_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='توضیحات کاربر در مورد خود'),
        ),
    ]
