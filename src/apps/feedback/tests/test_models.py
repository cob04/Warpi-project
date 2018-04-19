from django.test import TestCase

from ..factories import MetricFactory


class MetricMethodTests(TestCase):

    def test_string_representation(self):
        metric = MetricFactory.create()
        self.assertEqual(str(metric), "Happiness")

    def test_uuid_added_to_metric_only_on_creation(self):
        metric = MetricFactory.create()
        uuid = metric.uuid
        metric.save()
        self.assertEqual(uuid, metric.uuid)
