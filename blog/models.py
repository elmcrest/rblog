from django.utils.translation import gettext_lazy as _
from django.db import models
from main.models import Image


class Article(models.Model):
    created = models.DateTimeField(_("_created"), auto_now_add=True)
    updated = models.DateTimeField(_("_updated"), auto_now=True)
    published = models.DateTimeField(_("_published"))
    headline = models.CharField(_("_headline"), max_length=200)
    content = models.TextField(_("_content"))

    images = models.ManyToManyField(Image)

    def __str__(self):
        return f"<article {self.headline} {self.updated:'%d, %b, %Y'}>"

