from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('blog/<blog_id>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('category/<category_id>/', views.CategoryView.as_view(), name='category'),
    path('404/', views.NotFoundView.as_view(), name='404'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.CantactView.as_view(), name='contact')

]
