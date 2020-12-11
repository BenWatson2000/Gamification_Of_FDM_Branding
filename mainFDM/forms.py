from django import forms
from .models import GameQuestions

STREAM_TYPES = (
    ("Select", "Select Stream Type"),
    ("TOP", "Technical Operations"),
    ("BI", "Business Intelligence"),
    ("ST", "Software Testing"),
)


class AddQuestion(forms.Form):
    stream_type = forms.ChoiceField(widget=forms.Select, choices=STREAM_TYPES)
    question = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write the question here', 'rows': '3'}))
    answer = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write the correct answer here', 'rows': '2'}))


# dictionary variable for specifying all initial fields
# f = AddQuestion(initial={'qustion': 'Question'})
