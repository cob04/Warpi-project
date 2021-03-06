import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from apps.core.abstract_models import Slugged, TimeStamped
from apps.core.fields import OrderField

from . import fields


class Metric(TimeStamped, Slugged):
    """
    A model for details of a metric or category of feedback questions.
    """
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

    def get_absolute_url(self):
        return reverse("feedback:metric-form", args=[self.uuid])


class Question(TimeStamped, Slugged):
    """
    Details to be used  when displaying a question as a form field.
    """
    field_type = models.IntegerField(_("Form field type"), choices=fields.NAMES)
    choices = models.TextField(_("Choices"), max_length=1000, blank=True,
                               help_text="choices are delimited by a comma")
    help_text = models.CharField(_("Help text"), max_length=100, blank=True)
    placeholder = models.CharField(_("Placeholder"), max_length=100,
                                   blank=True)
    required = models.BooleanField(_("Required"), default=True)
    metric = models.ForeignKey("Metric", null=True, blank=True,
                               related_name="questions",
                               on_delete=models.CASCADE)
    order = OrderField(blank=True, for_fields=['metric'])

    def __str__(self):
        return "{}. {}".format(self.order + 1, self.title)

    def get_choices(self):
        """
        Parse a comma delimited choices string into a list of tupled choices.
        """
        choices = [(word.strip(), word.strip().capitalize())
                   for word in self.choices.split(",")]
        return choices


class Response(TimeStamped):
    """
    A response to the metric questions, this is then linked to
    the entries for each question.
    """
    metric = models.ForeignKey("Metric", null=True, blank=True,
                               related_name="responses",
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Response")
        verbose_name_plural = _("Responses")

    def __str__(self):
        return "{}".format(str(self.created))


class Entry(models.Model):
    response = models.ForeignKey("Response", null=True, blank=True,
                                 related_name="entries",
                                 on_delete=models.CASCADE)
    question_id = models.IntegerField()
    key = models.CharField(max_length=500, null=True)
    value = models.CharField(max_length=1000, null=True)
    data = JSONField()

    class Meta:
        verbose_name = _("Entry")
        verbose_name_plural = _("Entries")
