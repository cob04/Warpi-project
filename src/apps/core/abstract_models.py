################################
# PORJECT WIDE ABSTRACT MODELS #
################################


from django.db import models
from django.utils.translation import ugettext_lazy as _

from .utils import generate_unique_slug


class TimeStamped(models.Model):
    """
    Abstract model that provides creation and update timestamps
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Slugged(models.Model):
    """
    Abstract model provides a title and slug.
    The Slug is generated from the title.
    """
    title = models.CharField(_("Title"), max_length=255, db_index=True)
    slug = models.SlugField(_("Slug"), max_length=255, null=True, blank=True,
                            unique=True, db_index=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, "title", "slug")
        super().save()
