from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import View
from Blog.models import *
from Blog.forms import *
from site_settings.models import SiteSettings, SocialMedia
from main.forms import ArticleForm
from django.contrib import messages
from main.models import MainSeo


def media_url(request):
    return {'media_url': settings.MEDIA_URL}


class IndexView(View):
    template_name = 'page/main/index.html'

    def get(self, request):
        main_seo = MainSeo.objects.all()
        blogs = Blog.objects.filter(is_active=True).order_by('created_date')
        blog_view = Blog.objects.filter(is_active=True).order_by('-view_count')[:5]
        blog_views = Blog.objects.filter(is_active=True).order_by('-view_count')[:10]
        tags = BlogTag.objects.filter(blog__in=blogs)
        categories = BlogCategory.objects.all()
        category = BlogCategory.objects.all().order_by('-created_date')[:4]

        blog_category = []
        for cate in category:
            for blog in blogs.filter(category=cate):
                blog_category.append(blog)
        blog = Blog.objects.filter(is_active=True)[:4]
        selected_blog = Blog.objects.filter(selected=True, is_active=True).order_by('created_date')[:2]
        site_setting = SiteSettings.objects.all().first()
        social_media = SocialMedia.objects.all()

        top_best = Blog.objects.filter(is_active=True).order_by('-view_count')[:1]
        top = Blog.objects.filter(is_active=True, top=True).order_by('-view_count')[:3]
        form = ArticleForm()
        context = {
            'media_url': settings.MEDIA_URL,
            'blogs': blogs,
            'tags': tags,
            'blog_view': blog_view,
            'category': categories,
            'blog_views': blog_views,
            'blog_category': blog_category,
            'blog': blog,
            'selected_blog': selected_blog,
            'social_media': social_media,
            'top_best': top_best,
            'top': top,
            'form': form,
            'site_settings': site_setting,
            'main_seo': main_seo,
            'category_bottom':category
        }
        return render(request, self.template_name, context)


class SearchView(View):
    template_name = 'page/main/search.html'

    def get(self, request, *args, **kwargs):
        query = request.GET['q']
        blogs = Blog.objects.filter(title__icontains=query, is_active=True)
        blog_view = Blog.objects.filter(is_active=True).order_by('-view_count')[:5]
        site_setting = SiteSettings.objects.all().first()
        social_media = SocialMedia.objects.all()
        context = {
            'media_url': settings.MEDIA_URL,
            'blogs': blogs,
            'blog_view': blog_view,
            'site_settings': site_setting,
            'social_media': social_media
        }
        return render(request, self.template_name, context)


class BlogDetailView(View):
    template_name = 'page/main/blog_detail.html'

    def get(self, request, blog_id):
        form = CommentForm()
        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            messages.error(request, 'مقاله مورد نظر یافت نشد')
            return redirect('main:404')
        comments = BlogComment.objects.filter(blog=blog, is_active=True)
        comment_count = comments.count()
        site_setting = SiteSettings.objects.all().first()
        social_media = SocialMedia.objects.all()
        blog_view = Blog.objects.filter(is_active=True).order_by('-view_count')[:5]

        blog_category = Blog.objects.filter(category=blog.category)
        blog.view_count += 1
        blog.save()
        blog_seo = BlogSeo.objects.all()
        context = {
            'media_url': settings.MEDIA_URL,
            'blog': blog,
            'blog_category': blog_category,
            'form_comment': form,
            'comments': comments,
            'comment_count': comment_count,
            'social_media': social_media,
            'blog_view': blog_view,
            'site_settings': site_setting,
            'blog_seo': blog_seo
        }
        return render(request, self.template_name, context)

    def post(self, request, blog_id):
        form = CommentForm(request.POST)
        user = request.user
        blog = Blog.objects.get(id=blog_id)
        if form.is_valid():
            title = form.cleaned_data['title']
            comment = form.cleaned_data['comment']
            if user.is_authenticated:
                BlogComment.objects.create(author=user, comment=comment, blog=blog, title=title)
                messages.success(request, 'کامنت شما با موفقیت ثبت شد')
                return redirect('main:blog_detail', blog_id=blog.id)
            else:
                messages.error(request, 'ابتدا با ثبت نام کنید!!')
                return redirect('account:login')
        else:
            messages.error(request, 'فرم نامعتبر است')
            return redirect('main:blog_detail', blog_id=blog.id)


class CategoryView(View):

    def get(self, request, category_id):
        try:
            category = BlogCategory.objects.get(id=category_id)
        except BlogCategory.DoesNotExist:
            messages.error(request, 'دسته بندی یافت نشد')
            return redirect('main:404')
        site_setting = SiteSettings.objects.all().first()
        social_media = SocialMedia.objects.all()
        blog_view = Blog.objects.filter(is_active=True).order_by('-view_count')[:5]
        if category:
            context = {
                'category': category,
                'media_url': settings.MEDIA_URL,
                'social_media': social_media,
                'blog_view': blog_view,
                'site_settings': site_setting
            }
            return render(request, 'page/main/categories.html', context)


# region notfound
class NotFoundView(View):
    def get(self, request):
        site_setting = SiteSettings.objects.all().first()
        social_media = SocialMedia.objects.all()
        context = {
            'media_url': settings.MEDIA_URL,
            'social_media': social_media,
            'site_settings': site_setting
        }
        return render(request, 'page/main/404.html', context)


# endregion


class AboutView(View):
    def get(self, request):
        site_setting = SiteSettings.objects.all().first()
        social_media = SocialMedia.objects.all()
        context = {
            'media_url': settings.MEDIA_URL,
            'social_media': social_media,
            'site_settings': site_setting
        }
        return render(request, 'page/main/about.html', context)


class CantactView(View):
    def get(self, request):
        site_setting = SiteSettings.objects.all().first()
        social_media = SocialMedia.objects.all()
        context = {
            'media_url': settings.MEDIA_URL,
            'social_media': social_media,
            'site_settings': site_setting
        }
        return render(request, 'page/main/contact.html', context)
