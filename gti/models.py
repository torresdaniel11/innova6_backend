from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

#Modelo para la creacion de articulos.
class Articles(models.Model):
    article_tittle = models.CharField(max_length=200)
    article_content = models.TextField()
    article_slug = models.SlugField(editable=False)
    article_create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    article_update_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return self.article_tittle

    def save(self, *args, **kwargs):
        if not self.id:
            self.article_slug = slugify(self.article_tittle)
        super(Articles, self).save(*args, **kwargs)
