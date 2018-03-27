from django.conf.urls import url, include
from rest_framework import routers
from gti import views

router = routers.DefaultRouter()
router.register(r'articles', views.ArticleView)
router.register(r'conversations', views.ConversationView)

urlpatterns = [
    url(r'^', include(router.urls)),
]
