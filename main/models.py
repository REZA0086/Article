from django.db import models


# Create your models here.
class MainSeo(models.Model):
    SEO_TYPE = (('name', 'name'), ('property', 'property'))
    type = models.CharField(choices=SEO_TYPE, max_length=120)
    title = models.CharField(max_length=2000)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'seo اصلی'
        verbose_name_plural = 'seo اصلی'
