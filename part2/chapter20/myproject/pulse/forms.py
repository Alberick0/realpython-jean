__author__ = 'alberick'

from django import forms

class PulseForm(forms.Form):
    pulse = forms.CharField(label="What's the pulse:", max_length=50)