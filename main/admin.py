from django.contrib import admin
from main.models import MainSeo

@admin.register(MainSeo)
class MainSeoAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')