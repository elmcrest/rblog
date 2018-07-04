from django.utils.html import format_html, mark_safe
from django.views import generic

from content_editor.renderer import PluginRenderer
from content_editor.contents import contents_for_mptt_item

from .models import Article, RichText, Download

renderer = PluginRenderer()
renderer.register(RichText, lambda plugin: mark_safe(plugin.text))
renderer.register(
    Download,
    lambda plugin: format_html(f"<a href='{plugin.file.url}'>{plugin.file.name}</a>"),
)

# legacy view for testing, needs to be refactored for django-content-editor
class ArticleYearView(generic.ListView):
    model = Article

    def get_queryset(self):
        return Article.objects.filter(created__year=self.kwargs["year"])


class ArticleView(generic.DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            content=contents_for_mptt_item(
                self.object, [RichText, Download]
            ).render_regions(renderer),
            **kwargs,
        )

