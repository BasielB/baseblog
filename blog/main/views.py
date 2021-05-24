from django.shortcuts import render
from django.http import HttpResponse

from .models import Article, ContentImage


def display_all_articles(request):
    articles = Article.objects.all()
    return render(request, 'main/list_of_articles.html', {'articles': articles, 'title': 'Список статей'})
