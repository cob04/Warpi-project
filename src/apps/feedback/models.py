import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Metric(models.Model):
    """
    A model for details of a metric or category of feedback questions.
    """
    title = models.CharField(_("Title"), max_length=255)
    uuid = models.CharField(_("UUID"), max_length=100, unique=True,
                            null=True, blank=True)

    class Meta:
        verbose_name = _("Metric")
        verbose_name_plural = _("Metrics")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Create unique indentifiers
        # TODO: add in handling for then uuid generated is not unique.
        # rare as that may be.
        if not self.uuid:
            self.uuid = uuid.uuid4()
        super(Metric, self).save()
