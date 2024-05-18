from django.db import models
from django_jalali.db import models as jmodels
import jdatetime
from ckeditor_uploader.fields import RichTextUploadingField
from account.models import CustomerUser


class BlogCategory(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name='نام دسته بندی')
    picture = models.ImageField(upload_to='blog/category/', null=True, blank=True, verbose_name='تصویر دسته بندی')
    picture_alt = models.CharField(max_length=250, null=True, blank=True, verbose_name='متن جایگزین')
    picture_title = models.CharField(max_length=250, null=True, blank=True, verbose_name='عنوان تصویر')
    created_date = jmodels.jDateField(default=jdatetime.date.today(), verbose_name='تاریخ ساخت')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی مقاله ها'

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name='عنوان مقاله')
    text = RichTextUploadingField(config_name='special', verbose_name='توضیحات')
    created_date = jmodels.jDateField(default=jdatetime.date.today(), verbose_name='تاریخ ساخت')
    published_date = jmodels.jDateField(verbose_name='تاریخ تایید', null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name='تایید/عدم تایید')
    cover_image = models.ImageField(upload_to='media/article/', verbose_name='عکس مقاله')
    cover_title = models.CharField(max_length=2000, verbose_name='عنوان عکس مقاله')
    cover_alt = models.CharField(max_length=2000, verbose_name='متن جایگزین عکس')
    slug = models.SlugField()
    view_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    selected = models.BooleanField(default=False, verbose_name='منتخب')
    top = models.BooleanField(default=False, verbose_name='تایید برای بالا صفحه')

    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog_category',
                                 verbose_name='دسته بندی')
    author = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name='author',
                               verbose_name='نویسنده مقاله')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def save(self, *args, **kwargs):
        if self.is_active:
            self.published_date = jdatetime.date.today()
        else:
            self.published_date = None
        super(Blog, self).save(*args, **kwargs)


class BlogSeo(models.Model):
    SEO_TYPE = (('name', 'name'), ('property', 'property'))
    type = models.CharField(choices=SEO_TYPE, max_length=120)
    title = models.CharField(max_length=2000)
    content = models.TextField()

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'seo مقاله'
        verbose_name_plural = 'seo مقاله'


class CategorySeo(models.Model):
    SEO_TYPE = (('name', 'name'), ('property', 'property'))
    type = models.CharField(choices=SEO_TYPE, max_length=120)
    title = models.CharField(max_length=2000)
    content = models.TextField()

    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='category_seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'seo دسته بندی مقاله'
        verbose_name_plural = 'seo دسته بندی مقاله'


class BlogTag(models.Model):
    tag_name = models.CharField(max_length=2000, verbose_name="تگ مقاله")
    is_active = models.BooleanField(default=False, verbose_name="تایید / عدم تایید")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="مقاله", related_name="tag_blog")

    class Meta:
        verbose_name = 'تگ مقاله'
        verbose_name_plural = 'تگ مقالات'

    def __str__(self):
        return f'{self.tag_name} - {self.blog}'


class BlogComment(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان کامنت")
    comment = RichTextUploadingField(config_name='special', verbose_name='متن کامنت')
    created_date = jmodels.jDateField(default=jdatetime.date.today(), verbose_name='تاریخ ساخت')
    published_date = jmodels.jDateField(null=True, blank=True, verbose_name='تاریخ تایید')
    is_active = models.BooleanField(default=False, verbose_name='تایید/عدم تایید')

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='مقاله')
    author = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, verbose_name='نویسنده کامنت')

    class Meta:
        verbose_name = 'کامنت مقاله'
        verbose_name_plural = 'کامنت مقالات'

    def __str__(self):
        return f'{self.author}-{self.blog}'

    def save(self, *args, **kwargs):
        if self.is_active:
            self.published_date = jdatetime.date.today()
        else:
            self.published_date = None
        super(BlogComment, self).save(*args, **kwargs)
