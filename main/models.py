from django.db import models
from django.utils.translation import gettext_lazy as _

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Image(models.Model):
    image = models.ImageField(upload_to="original_images")
    main_image = ImageSpecField(
        source="image",
        processors=[ResizeToFill(100, 50)],
        format="JPEG",
        options={"quality": 60},
    )
    caption = models.CharField(_("_caption"), max_length=200)
