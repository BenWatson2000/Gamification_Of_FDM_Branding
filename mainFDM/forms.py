from django import forms

STREAM_TYPES = (
    ("Select", "Select Stream Type"),
    ("TOP", "Technical Operations"),
    ("BI", "Business Intelligence"),
    ("ST", "Software Testing"),
)

class AddQuestion(forms.Form):
    stream_type = forms.ChoiceField(widget=forms.Select, choices=STREAM_TYPES)
    question = forms.CharField()
    answer = forms.CharField()
    incorrect1 = forms.CharField()
    incorrect2 = forms.CharField()

# dictionary variable for specifying all initial fields
# f = AddQuestion(initial={'qustion': 'Question'})
