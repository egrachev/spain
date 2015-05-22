# -*- coding: utf-8 -*-

from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', 'main.views.index', name='index'),
    url(r'^sitemap.xml$', 'main.views.sitemap_xml', name='sitemap_xml'),
    url(r'^sitemap.xsl$', 'main.views.sitemap_xsl', name='sitemap_xsl'),

    url(r'^(?P<slug>[-\w]+)$', 'main.views.page_view', name='page_view'),
]