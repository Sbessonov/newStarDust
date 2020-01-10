from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Article, Comment


# Create your views here.


def index(request):
    latest = Article.objects.order_by('-pub_date')[:10]
    return render(request, 'articles/list_articles.html', {'latest': latest})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except Exception:
        raise Http404('Статья не найдена')
    return render(request, 'articles/detail.html', {'article': a})
