from django import forms
from django.core import validators

class Member(forms.Form):
    name = forms.CharField(label="Full name", initial = 'Name', max_length = 100)
    email = forms.EmailField(help_text = 'write your email', )
    phone = forms.CharField(help_text = 'write your phone', validators = [validators.MinLengthValidator(10)])
    note = forms.CharField(help_text = 'write your note', widget = forms.Textarea, required = False)