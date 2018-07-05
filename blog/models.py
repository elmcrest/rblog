from django.utils.translation import gettext_lazy as _
from django.db import models

from content_editor.models import Template, Region, create_plugin_base
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# class Image(models.Model):
#     image = models.ImageField(upload_to="original_images")
#     main_image = ImageSpecField(
#         source="image",
#         processors=[ResizeToFill(100, 50)],
#         format="JPEG",
#         options={"quality": 60},
#     )
#     caption = models.CharField(_("_caption"), max_length=200)


class Article(models.Model):
    created = models.DateTimeField(_("_created"), auto_now_add=True)
    updated = models.DateTimeField(_("_updated"), auto_now=True)
    headline = models.CharField(_("_headline"), max_length=200)
    slug = models.SlugField(_("_slug"), max_length=200)

    regions = [
        Region(key="main", title="main region"),
        Region(key="sidebar", title="sidebar region", inherited=False),
    ]

    class Meta:
        unique_together = (("slug", "created"),)
        ordering = ["-updated"]

    def get_absolute_url(self):
        return f"/blog/{self.created.year}/{self.created.month}/{self.slug}"

    def get_unique_identifier(self):
        return f"{self.created.year}_{self.created.month}_{self.slug}"

    def __str__(self):
        return self.headline


ArticlePlugin = create_plugin_base(Article)


class RichText(ArticlePlugin):
    text = models.TextField(blank=True)

    class Meta:
        verbose_name = _("_richtext")
        verbose_name_plural = _("_richtexts")


class Image(ArticlePlugin):
    image = models.ImageField(upload_to="images/%Y/%m")
    alt = models.CharField(max_length=200)

    class Meta:
        verbose_name = _("_image")
        verbose_name_plural = _("_images")


class Download(ArticlePlugin):
    file = models.FileField(upload_to="download/%Y/%m")

    class Meta:
        verbose_name = _("_downloaditem")
        verbose_name_plural = _("_downloaditems")


class Menu(models.Model):
    # simple Menu Class to create Menus out of existing Article objects
    name = models.CharField(_("_name"), max_length=200)
    items = models.ManyToManyField(Article, through="MenuItem")

    def __str__(self):
        return f"{self.name}"


class MenuItem(models.Model):
    article = models.ForeignKey(Article, on_delete=models.PROTECT)
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    order = models.IntegerField()
