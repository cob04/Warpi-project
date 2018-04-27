from django.contrib import admin

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
    readonly_fields = ("question_id", "key", "value")

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('created',)
    inlines = [EntryInline]
