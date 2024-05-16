from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class SiteSettings(models.Model):
    title = models.CharField(max_length=250, verbose_name='عنوان سایت',null=True,blank=True)
    favicon = models.ImageField(upload_to='media/', verbose_name='فاوآیکون',null=True,blank=True)
    logo = models.ImageField(upload_to='media/', verbose_name='لوگوی سایت',null=True,blank=True)
    logo_url = models.CharField(max_length=250, null=True, verbose_name='url لوگو')
    phone_number = models.CharField(max_length=11, verbose_name='شماره تلفن',null=True,blank=True)
    logo_alt = models.CharField(max_length=250, verbose_name='متن جایگزین لوگو', null=True, blank=True)
    logo_title = models.CharField(max_length=250, verbose_name='عنوان لوگو', null=True, blank=True)
    about_us = RichTextUploadingField(config_name='special', verbose_name='درباره ما', null=True, blank=True)
    email = models.EmailField(max_length=254, verbose_name='ایمیل', null=True, blank=True)
    address = models.CharField(max_length=250, verbose_name='آدرس', null=True, blank=True)
    text_footer = RichTextUploadingField(config_name='special', verbose_name='متن پایین صفحه', null=True, blank=True)
    text_contact = RichTextUploadingField(config_name='special', verbose_name='متن تماس با ما', null=True, blank=True)

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'


class SocialMedia(models.Model):
    name = models.CharField(max_length=250, verbose_name='نام شبکه')
    url = models.CharField(max_length=250, verbose_name='url شبکه')
    logo = models.ImageField(upload_to='media/', verbose_name='لوگوی شبکه', null=True, blank=True)
    logo_url = models.CharField(max_length=250, null=True,verbose_name='url لوگو' )
    logo_alt = models.CharField(max_length=250, verbose_name='متن جایگزین لوگو', null=True, blank=True)
    logo_title = models.CharField(max_length=250, verbose_name='عنوان لوگو', null=True, blank=True)

    class Meta:
        verbose_name = 'شبکه های اجتماعی'
        verbose_name_plural = 'شبکه های اجتماعی'
