from django import forms

STREAM_TYPES = (
    ("Select", "Select Stream Type"),
    ("TOP", "Technical Operations"),
    ("BI", "Business Intelligence"),
    ("ST", "Software Testing"),
)


class AddQuestion(forms.Form):
    stream_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select mb-3', 'aria-label': 'Default '
                                                                                                          'select '
                                                                                                          'example'}),
                                    choices=STREAM_TYPES)
    question = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height:100px',
                                                            'placeholder': 'Add your question here!',
                                                            'id': 'floatingTextarea'}))
    answer = forms.CharField(widget=forms.Textarea(attrs={'type': "text", 'class': 'form-control', 'style': 'height: '
                                                                                                            '70px',
                                                          'placeholder': 'Add the correct answer here',
                                                          'id': 'floatingAnswer'}))


class HighestScore(forms.Form):
    highest_score = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Highest Score', 'aria-label': 'Highest Score'}))
