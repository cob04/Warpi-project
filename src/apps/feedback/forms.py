from django import forms
from django.utils.timezone import now

from . import fields
from .models import Response, Entry
from .widgets import StarRatingWidget


class ResponseModelForm(forms.ModelForm):
    """
    Dynamically add fields from the passed in question instances(plural).
    """
    class Meta:
        model = Response
        exclude = ("metric",)

    def __init__(self, metric, *args, **kwargs):
        """
        Dynamically add each of the form fields to the given questions.
        """
        self.metric = metric
        self.questions = metric.questions.all()
        super(ResponseModelForm, self).__init__(*args, **kwargs)

        for question in self.questions:
            field_key = "question_%d" % question.id
            field_class = fields.CLASSES[question.field_type]
            firld_widget = fields.WIGETS.get(question.field_type)

            field_args = {
                "label": str(question),
                "required": question.required,
                "help_text": question.help_text,
            }

            arg_names = field_class.__init__.__code__.co_varnames

            if "choices" in arg_names:
                field_args["choices"] = question.get_choices()

            if field_widget is not None:
                field_args["widget"] = field_widget

            self.fields[field_key] = field_class(**field_args)

    def save(self, **kwargs):
        """
        Save the response data as json to the Response instance.
        """
        response = super(ResponseModelForm, self).save(commit=False)
        response.metric = self.metric
        response.save()
        new_response_entries = []

        for question in self.questions:
            field_key = "question_%d" % question.id
            value = self.cleaned_data[field_key]

            if isinstance(value, list):
                value = ", ".join([v.strip() for v in value])

            new = {
                "response": response,
                "question_id": question.id,
                "key": str(question),
                "value": value
            }
            new_response_entries.append(Entry(**new))

        if new_response_entries:
            Entry.objects.bulk_create(new_response_entries)

        return response
