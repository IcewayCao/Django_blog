# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


def article_edit(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/article_edit.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_edit.html', {'article': article})


def article_delete(request, article_id):
    models.Article.objects.get(pk=article_id).delete()
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', 0)

    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})

