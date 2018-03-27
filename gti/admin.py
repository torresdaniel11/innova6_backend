from django.contrib import admin
from .models import Articles
from .models import ConversationLevels
from .models import Conversations


# Register your models here.
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('article_tittle', 'article_create_date', 'article_update_date')


admin.site.register(Articles, ArticlesAdmin)


class ConversationLevelsAdmin(admin.ModelAdmin):
    list_display = ('conversation_level_name', 'conversation_color')


admin.site.register(ConversationLevels, ConversationLevelsAdmin)


class ConversationsAdmin(admin.ModelAdmin):
    list_display = (
        'conversation_token', 'conversation_name', 'conversation_email', 'conversation_platform',
        'conversation_faculty',
        'conversation_create_date', 'conversation_update_date', 'conversation_conversation_level')


admin.site.register(Conversations, ConversationsAdmin)
