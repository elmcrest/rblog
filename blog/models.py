from django.utils.translation import gettext_lazy as _
from django.db import models

from content_editor.models import Template, Region, create_plugin_base


class Article(models.Model):
    created = models.DateTimeField(_("_created"), auto_now_add=True)
    updated = models.DateTimeField(_("_updated"), auto_now=True)
    published = models.DateTimeField(_("_published"))
    headline = models.CharField(_("_headline"), max_length=200)

    regions = [
        Region(key="main", title="main region"),
        Region(key="sidebar", title="sidebar region", inherited=False),
    ]

    def __str__(self):
        return f"<article {self.headline} {self.updated:'%d, %b, %Y'}>"


ArticlePlugin = create_plugin_base(Article)


class RichText(ArticlePlugin):
    text = models.TextField(blank=True)

    class Meta:
        verbose_name = "rich text"
        verbose_name_plural = "rich texts"


class Download(ArticlePlugin):
    file = models.FileField(upload_to="download/%Y/%m")

    class Meta:
        verbose_name = "download"
        verbose_name_plural = "downloads"
