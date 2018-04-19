from django.contrib import admin

from .models import Metric, Question



class QuestionInline(admin.StackedInline):
    model =  Question


@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ('title',)
    readonly_fields = ('uuid',)
    inlines = [QuestionInline]
