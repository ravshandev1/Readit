from django.shortcuts import render
from .models import *
from .forms import CommentForm


# Create your views here.

def home(request):
    articles = Article.objects.order_by('-id')
    ctx = {
        'articles': articles,
    }
    return render(request, 'index.html', ctx)


def blog(request):
    articles = Article.objects.order_by('-id')
    ctx = {
        'articles': articles,
    }
    return render(request, 'blog.html', ctx)


def blog_single(request, pk):
    article = Article.objects.get(id=pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    articles = Article.objects.order_by('-id')
    form = CommentForm(request.POST or None, request.FILES)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
    ctx = {
        'article': article,
        'categories': categories,
        'tags': tags,
        'last_articles': articles[:3],
        'form': form
    }
    return render(request, 'blog-single.html', ctx)
