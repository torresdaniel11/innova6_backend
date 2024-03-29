from django.conf.urls import url, include
from rest_framework import routers
from gti import views

suggested_questions = views.ConversationView.as_view({
    'get': 'suggested_questions_get',
    'post': 'save_response_suggested_questions_post'
})

suggested_questions_records = views.ConversationView.as_view({
    'get': 'retrieve_response_suggested_questions_post',
})

router = routers.DefaultRouter()
router.register(r'articles', views.ArticleView)
router.register(r'conversations', views.ConversationView)
router.register(r'questions', views.QuestionView)
router.register(r'categories', views.CategoryView)
router.register(r'question_articles', views.QuestionArticlesView)
router.register(r'conversation_levels', views.ConversationLevelsView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^conversations/(?P<conversation_token>[^/.]+)/questions/$', suggested_questions, name='suggested-questions'),
    url(r'^question_records/(?P<conversation_token>[^/.]+)/questions/$', suggested_questions,
        name='save-response-suggested_questions_post'),
    url(r'^question_records/(?P<conversation_token>[^/.]+)/$', suggested_questions_records,
        name='save-response-suggested_questions_post')
]
