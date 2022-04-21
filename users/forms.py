from django import forms
from .models import Player


class PlayerForm(forms.Form):
    test = forms.IntegerField()
    testname = forms.CharField()
