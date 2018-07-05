from django.utils.html import format_html, mark_safe
from django.views import generic
from django.http import Http404

from content_editor.renderer import PluginRenderer
from content_editor.contents import contents_for_item

from .models import Article, RichText, Download, Image, Menu, MenuItem

renderer = PluginRenderer()
renderer.register(RichText, lambda plugin: mark_safe(plugin.text))
renderer.register(
    Download,
    lambda plugin: format_html(f"<a href='{plugin.file.url}'>{plugin.file.name}</a>"),
)
renderer.register(
    Image,
    lambda plugin: format_html(f"<img src='{plugin.image.url}' alt='{plugin.alt}'/>"),
)


class ArticleYearView(generic.ListView):
    model = Article

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            mainmenu=MenuItem.objects.filter(menu__name="mainmenu")
            .order_by("order")
            .all(),
            **kwargs,
        )

    def get_queryset(self):
        kwargs = self.kwargs
        queryset = Article.objects.exclude(menuitem__isnull=False)
        if kwargs.get("year", False):
            return queryset.filter(created__year=kwargs["year"])
        elif kwargs.get("month", False):
            return queryset.filter(
                created__year=kwargs["year"], created__month=kwargs["month"]
            )
        else:
            return queryset.all()


class ArticleView(generic.DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            content=contents_for_item(
                self.object, [RichText, Download, Image]
            ).render_regions(renderer),
            mainmenu=MenuItem.objects.filter(menu__name="mainmenu")
            .order_by("order")
            .all(),
            **kwargs,
        )

    def get_object(self):
        try:
            return (
                Article.objects.filter(created__year=self.kwargs["year"])
                .filter(created__month=self.kwargs["month"])
                .get(slug=self.kwargs["slug"])
            )
        except Article.DoesNotExist:
            raise Http404("No Article matches the given query.")


class ArticleExtraView(ArticleView):
    def get_object(self):
        kwargs = self.kwargs
        try:
            if kwargs.get("slug", False):
                return Article.objects.order_by("updated").get(slug=kwargs["slug"])
            else:
                # return home view, which is by convention the article with headline "about"
                return Article.objects.get(slug="about")
        except Article.DoesNotExist:
            raise Http404("No Article matches the given query.")
