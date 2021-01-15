
from django import forms
from django.forms import ModelForm
from clubs.models import Survey

class addSurveyForm(ModelForm):
    question = forms.Textarea()
    end_date = forms.DateTimeField(label="Pick Up Date",
                                   widget=forms.DateTimeInput(attrs={
                                       "type": "datetime-local", "name": "tookDate", "id": "first", "min": "",
                                       "class": "form-control datepicker px-3"
                                   }))

    class Meta:
        model = Survey
        fields = ['question','element1','element2','end_date']

