from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from mainFDM.models import Score

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


# TODO customise the login form in the same way (somehow)


class CreateHelperForm(UserCreationForm):
    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'style': 'height:max-content',
                                                                  'title': 'Enter your password',
                                                                  'placeholder': 'Enter your password...',
                                                                  'id': 'floatingPassword1'}))
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'style': 'height:max-content',
                                                                  'title': 'Repeat your password',
                                                                  'placeholder': 'Confirm your password...',
                                                                  'id': 'floatingPassword2'}),
                                help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'style': 'height:max-content',
                                               'placeholder': 'Enter your username...',
                                               'title': 'Enter your username here',
                                               'id': 'floatingUsername'}),
            'email': forms.TextInput(attrs={'type': "text", 'class': 'form-control',
                                            'style': 'height:max-content',
                                            'placeholder': 'Enter your email address...',
                                            'title': 'Enter your email address',
                                            'id': 'floatingEmail'}),
        }


class AddScores(ModelForm):
    class Meta:
        model = Score
        fields = ['player_username', 'game_type', 'score']
        labels = {
            'player_username': _('Please enter your username:'),
            'game_type': _('Game you played:'),
            'score': _('Your score:')
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(player_username)s's %(game_type)s are not unique.",
            }
        }
        widgets = {
            'player_username': forms.TextInput(attrs={'class': 'form-control',
                                                      'style': 'height:max-content',
                                                      'placeholder': 'Username',
                                                      'title': 'Enter your username here',
                                                      'id': 'floatingUsername'}),
            'game_type': forms.TextInput(attrs={'type': "text", 'class': 'form-control form-readonly',
                                                'style': 'height:max-content',
                                                'placeholder': 'Game type',
                                                'title': 'This is the game you played',
                                                'id': 'floatingGame', 'disabled': True}),
            'score': forms.TextInput(attrs={'type': "text", 'class': 'form-control form-readonly',
                                            'style': 'height:max-content',
                                            'placeholder': 'Your Score',
                                            'title': 'This is your score',
                                            'id': 'floatingScore', 'disabled': True})
        }