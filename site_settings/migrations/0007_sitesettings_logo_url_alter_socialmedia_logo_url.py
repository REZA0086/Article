# Generated by Django 5.0.6 on 2024-05-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0006_sitesettings_text_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='logo_url',
            field=models.CharField(max_length=250, null=True, verbose_name='url لوگو'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='logo_url',
            field=models.CharField(max_length=250, null=True, verbose_name='url لوگو'),
        ),
    ]
