from django.contrib import admin
from .models import Articles
from .models import ConversationLevels
from .models import Conversations
from .models import Questions
from .models import QuestionArticles
from .models import QuestionRecords


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


class QuestionsAdmin(admin.ModelAdmin):
    list_display = (
        'question_name', 'question_description', 'question_keywords', 'question_conversation_level')


admin.site.register(Questions, QuestionsAdmin)


class QuestionArticlesAdmin(admin.ModelAdmin):
    list_display = (
        'question_article_name', 'question_article_description', 'question_article_keywords',
        'question_article_question')


admin.site.register(QuestionArticles, QuestionArticlesAdmin)


class QuestionRecordsAdmin(admin.ModelAdmin):
    list_display = (
        'question_record_response', 'question_record_conversation', 'question_record_question', 'question_record_token',
        'question_record_create_date')


admin.site.register(QuestionRecords, QuestionRecordsAdmin)
