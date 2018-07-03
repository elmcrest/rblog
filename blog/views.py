from django.views.generic import ListView
from .models import Article


class ArticleYearView(ListView):
    model = Article

    def get_queryset(self):
        return Article.objects.filter(created__year=self.kwargs["year"])
