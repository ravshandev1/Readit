from django import template
from articles.models import Article

register = template.Library()


@register.simple_tag()
def last_articles():
    try:
        articles = Article.objects.order_by('-id')[:2]
    except:
        articles = None
    return articles
