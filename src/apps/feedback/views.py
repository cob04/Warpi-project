from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import View


from .forms import ResponseModelForm
from .models import Metric


class MetricMixin(object):
    """
    Mixin to fetch current feedback metric in view. It also prefetches questions
    related to a metric instance.
    """
    query = Metric.objects.prefetch_related("questions").all()

    def get_metric_by_id(self):
        return get_object_or_404(self.query, pk=self.kwargs['pk'])

    def get_metric_by_uuid(self):
        return get_object_or_404(self.query, uuid=self.kwargs['uuid'])


class FeedbackMetricView(MetricMixin, View):
    template_name = "feedback/metric_form.html"

    def get(self, request, *args, **kwargs):
        context = {}
        metric = self.get_metric_by_uuid()
        metric_form = ResponseModelForm(metric)
        metric_list = Metric.objects.all()
        context['form'] = metric_form
        context['metric'] = metric
        context['metric_list'] = metric_list
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        metric = self.get_metric_by_uuid()
        metric_form = ResponseModelForm(metric, request.POST)
        metric_form.save()
        return redirect('/')


class MetricListView(ListView):
    template_name = "feedback/index.html"
    model = Metric
