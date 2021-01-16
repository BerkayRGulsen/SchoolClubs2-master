from django import forms
from django.forms import ModelForm
from clubs.models import *

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
        widgets = {
            'question': forms.Textarea(attrs={'rows': 2, 'cols': 50}),
        }


class addPostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['content', 'post_pic']

        widgets = {
            'content' : forms.Textarea(attrs={'rows':5, 'cols':50}),
        }


class addDiscussionForm(ModelForm):
    class Meta:
        model = Discussion
        fields = ['topic','content']

        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
            'topic': forms.Textarea(attrs={'rows': 1, 'cols': 50})
        }


