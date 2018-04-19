import factory

from .models import Metric


class MetricFactory(factory.DjangoModelFactory):

    class Meta:
        model = Metric

    title = "Happiness" # are our customers happy?
