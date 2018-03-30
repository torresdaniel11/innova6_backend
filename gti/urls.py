from django.conf.urls import url, include
from rest_framework import routers
from gti import views

suggested_questions = views.ConversationView.as_view({
    'get': 'suggested_questions'
})

router = routers.DefaultRouter()
router.register(r'articles', views.ArticleView)
router.register(r'conversations', views.ConversationView)
router.register(r'questions', views.QuestionView)
router.register(r'categories', views.CategoryView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^conversations/(?P<conversation_token>[^/.]+)/questions/$', suggested_questions, name='suggested-questions'),
]
