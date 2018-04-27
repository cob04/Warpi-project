from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.MetricListView.as_view(),
        name="metric_list"),
    url(r'^(?P<uuid>[-\w]+)/$', views.FeedbackMetricView.as_view(),
        name="metric-form"),
]
