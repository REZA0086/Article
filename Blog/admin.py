from django.contrib import admin
from Blog.models import *


def active_blog(modeladmin, request, queryset):
    res = queryset.update(is_active=True)
    message = f'تعداد {res} مقاله فعال شد'
    modeladmin.message_user(request, message)


def de_active_blog(modeladmin, request, queryset):
    res = queryset.update(is_active=True)
    message = f'تعداد {res} مقاله غیرفعال شد'
    modeladmin.message_user(request, message)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'category')

    actions = [active_blog, de_active_blog]

    active_blog.short_description = 'فعال کردن مقاله های انتخابی'
    de_active_blog.short_description = 'غیرفعال کردن مقاله های انتخابی'


@admin.register(BlogSeo)
class BlogSeoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')

@admin.register(CategorySeo)
class CategorySeoAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('tag_name','is_active','blog')
    list_editable = ['is_active']


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('title','blog','author','is_active')
    list_editable = ['is_active']


