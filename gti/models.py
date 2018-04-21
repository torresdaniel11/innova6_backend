from __future__ import unicode_literals

import binascii
import os

from django.db import models
from django.template.defaultfilters import slugify


class ConversationLevels(models.Model):
    conversation_level_name = models.CharField(max_length=200)
    conversation_color = models.CharField(max_length=200)

    def __unicode__(self):
        return self.conversation_level_name

    def save(self, *args, **kwargs):
        super(ConversationLevels, self).save(*args, **kwargs)


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)


class Conversations(models.Model):
    conversation_token = models.CharField(max_length=200, editable=False)
    conversation_name = models.CharField(max_length=200, blank=True)
    conversation_email = models.CharField(max_length=200, blank=True)
    conversation_platform = models.CharField(max_length=200, blank=True)
    conversation_faculty = models.CharField(max_length=200, blank=True)
    conversation_create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    conversation_update_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    conversation_conversation_level = models.ForeignKey(ConversationLevels, editable=False, null=True, blank=True,
                                                        on_delete=models.DO_NOTHING)


    def __unicode__(self):
        return self.conversation_token

    def generate_key(self):
        return binascii.hexlify(os.urandom(30)).decode()

    def save(self, *args, **kwargs):
        if not self.id:
            self.conversation_token = self.generate_key()
        super(Conversations, self).save(*args, **kwargs)


class EvaluateConversation(models.Model):
    evaluate_conversation_score = models.CharField(max_length=200)
    evaluate_conversation_observation = models.TextField()
    evaluate_conversation_conversation = models.ForeignKey(Conversations, null=True, blank=True,
                                                           on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        super(EvaluateConversation, self).save(*args, **kwargs)


class Questions(models.Model):
    question_name = models.CharField(max_length=200)
    question_description = models.TextField()
    question_keywords = models.TextField()
    question_conversation_level = models.ForeignKey(ConversationLevels, null=True, blank=True,
                                                    on_delete=models.DO_NOTHING)
    question_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.DO_NOTHING)
    question_update = models.BooleanField(default=False)
    question_replace = models.BooleanField(default=False)
    question_load_question = models.BooleanField(default=False)
    question_load_article = models.BooleanField(default=False)
    question_evaluate_one = models.BooleanField(default=False)
    question_evaluate_two = models.BooleanField(default=False)
    question_field_update = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.question_name

    def save(self, *args, **kwargs):
        super(Questions, self).save(*args, **kwargs)


class QuestionArticles(models.Model):
    question_article_name = models.CharField(max_length=200)
    question_article_description = models.TextField()
    question_article_keywords = models.TextField()
    question_article_question = models.ForeignKey(Questions, null=True, blank=True,
                                                  on_delete=models.DO_NOTHING)
    question_article_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.question_article_name

    def save(self, *args, **kwargs):
        super(QuestionArticles, self).save(*args, **kwargs)


class QuestionRecords(models.Model):
    question_record_response = models.TextField()
    question_record_conversation = models.ForeignKey(Conversations,
                                                     on_delete=models.CASCADE)
    question_record_question = models.ForeignKey(Questions,
                                                 on_delete=models.DO_NOTHING)
    question_record_token = models.CharField(max_length=200, editable=False, blank=True, null=True)
    question_record_create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        super(QuestionRecords, self).save(*args, **kwargs)


class Articles(models.Model):
    article_tittle = models.CharField(max_length=200)
    article_content = models.TextField()
    article_slug = models.SlugField(editable=False)
    article_create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    article_update_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    question_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.article_tittle

    def save(self, *args, **kwargs):
        if not self.id:
            self.article_slug = slugify(self.article_tittle)
        super(Articles, self).save(*args, **kwargs)
