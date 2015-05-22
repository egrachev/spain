# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Page


def index(request):
    return render(request, 'index.html')

def page_view(request, slug):
    page = Page.objects.get(slug=slug)

    return render(request, 'page.html', {
        'page': page,
    })

def sitemap_xml(request):
    pages = Page.objects.all()
    return render(request, 'sitemap.xml', {'pages': pages}, content_type='text/xml')

def sitemap_xsl(request):
    return render(request, 'sitemap.xsl', content_type='text/xsl')
