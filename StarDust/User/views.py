from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, JsonResponse
from .models import Article, Comment
from django.urls import reverse
from django.core import serializers
import simplejson as sj
from django.http import HttpResponse

# Create your views here.


def index(request):
    latest = Article.objects.order_by('-pub_date')
    return render(request, 'articles/list_articles.html', {'latest': latest})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except Exception:
        raise Http404('Статья не найдена')
    comments_list = a.comment_set.order_by('-id')
    send_info = a.to_dict()
    comments_dict = []
    for comment in comments_list:
        comments_dict.append(comment.to_dict())
    send_info['comments'] = comments_dict
    return JsonResponse(send_info, )

def register_user(request):
    pass


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except Exception:
        raise Http404('Статья не найдена')
    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('detail', args=(a.id,)))