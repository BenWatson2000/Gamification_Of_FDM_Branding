from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

STREAM_TYPES = (
    ("", "Select Stream Type"),
    ("TOP", "Technical Operations"),
    ("BI", "Business Intelligence"),
    ("ST", "Software Testing"),
)


class AddQuestion(forms.Form):
    stream_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select mb-3',
                                                               'title': 'Choose the stream type here!',
                                                               'placeholder': 'Select Stream Type',
                                                               'aria-label': 'Default select', 'id': 'floatingSelect'}),
                                    choices=STREAM_TYPES)
    question = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height:100px',
                                                            'placeholder': 'Question',
                                                            'title': 'Add your question here!',
                                                            'id': 'floatingQuestion'}))

    answer = forms.CharField(widget=forms.Textarea(attrs={'type': "text", 'class': 'form-control',
                                                          'style': 'height: 70px', 'placeholder': 'Answer',
                                                          'title': 'Add the correct answer here!',
                                                          'id': 'floatingAnswer'}))


class CreateHelperForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# This form has been replaced with a HTML version and it might stay like this but not deleting for now
# class HighestScore(forms.Form):
#     highest_score = forms.CharField(widget=forms.TextInput(
#         attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Highest Score',
#         'aria-label': 'Highest Score'}))
