import factory

from .models import Metric, Question


class MetricFactory(factory.DjangoModelFactory):

    class Meta:
        model = Metric

    title = "Happiness" # are our customers happy?


class QuestionFactory(factory.DjangoModelFactory):

    class Meta:
        model = Question

    title = "From 1 to 5 How happy are you?"
    field_type = 1
    metric = factory.SubFactory(MetricFactory)
