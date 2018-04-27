from django.test import TestCase

from ..factories import MetricFactory, QuestionFactory


class MetricMethodTests(TestCase):

    def test_string_representation(self):
        metric = MetricFactory.create()
        self.assertEqual(str(metric), "Happiness")

    def test_uuid_added_to_metric_only_on_creation(self):
        metric = MetricFactory.create()
        uuid = metric.uuid
        metric.save()
        self.assertEqual(uuid, metric.uuid)

    def test_fetching_absolute_url(self):
        metric = MetricFactory.create()
        self.assertEqual(metric.get_absolute_url(), "/feedback/%s/" % metric.uuid)


class QuestionMethodTests(TestCase):

    def setUp(self):
        self._metric = MetricFactory.create()

    def test_string_representation(self):
        question = QuestionFactory.create(metric=self._metric)
        self.assertEqual(str(question),
                         "From 1 to 5 How happy are you?")

    def test_getting_choices_tuples(self):
        question = QuestionFactory.create(
            metric=self._metric,
            choices="one, two, three, four, five"
        )
        choices = question.get_choices()
        self.assertEqual(choices,
                         [('one', 'One'),
                          ('two', 'Two'),
                          ('three', 'Three'),
                          ('four', 'Four'),
                          ('five', 'Five')
                         ])
