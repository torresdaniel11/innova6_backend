from django.contrib import admin
from .models import Articles

# Register your models here.
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('article_tittle', 'article_create_date', 'article_update_date')

admin.site.register(Articles, ArticlesAdmin)