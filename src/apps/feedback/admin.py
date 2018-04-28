import json

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import HtmlFormatter

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Entry, Metric, Question, Response


class QuestionInline(admin.StackedInline):
    model =  Question
    readonly_fields = ('order',)

@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ('title',)
    readonly_fields = ('uuid',)
    inlines = [QuestionInline]


class EntryInline(admin.TabularInline):
    model = Entry
    readonly_fields = ("question_id", "key", "value", "data_prettified")
    exclude = ('data',)
    extra = 0

    def data_prettified(self, instance):
        response = json.dumps(instance.data, sort_keys=True, indent=2)
        response = response[:2000]
        formatter = HtmlFormatter(style='colorful')
        response = highlight(response, JsonLexer(), formatter)
        style="<style>" + formatter.get_style_defs() + "</style>"
        return mark_safe(style + response)

    data_prettified.short_description = 'data'


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('created',)
    inlines = [EntryInline]
