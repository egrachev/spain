# -*- coding: utf-8 -*-

from django.db import models


class Page(models.Model):
    title = models.CharField(u'Заголовок', max_length=50)
    slug = models.SlugField(u'Служебное поле')
    text = models.TextField(u'Текст')

    def __unicode__(self):
        return self.title
