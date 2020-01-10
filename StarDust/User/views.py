from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Article, Comment


# Create your views here.


def index(request):
    latest = Article.objects.order_by('-pub_date')[:2]
    return render(request, 'articles/list_articles.html', {'latest': latest})


def detail(request, article_id):
    a = Article.objects.order_by('-pub_date')[:3]
    return render(request, 'articles/list_articles.html', {'latest': a})
