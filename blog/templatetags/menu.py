from collections import defaultdict
from django import template
from django.db.models import Q
from blog.models import Article

register = template.Library()


@register.simple_tag
def menu():
    menu = list()
    articles = Article.objects.filter(in_menu=True).order_by("menu_order")
    for article in articles:
        menu.append(article)
    return ["articles"] + menu
