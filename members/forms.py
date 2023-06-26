from django import forms
from django.core import validators
from .models import Company

class Member(forms.Form):
    name = forms.CharField(label="Full name", initial = 'Name', max_length = 100)
    email = forms.EmailField(help_text = 'write your email', )
    phone = forms.CharField(help_text = 'write your phone', validators = [validators.MinLengthValidator(10)])
    company = forms.ModelChoiceField(queryset=Company.objects.order_by('name'), empty_label='----', widget=forms.Select())
    note = forms.CharField(help_text = 'write your note', widget = forms.Textarea, required = False)
    password = forms.CharField(widget = forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError("Password is too short")
        return password

class Company(forms.Form):
    name = forms.CharField(label="Full name", initial = 'Name', max_length = 100)
    address = forms.CharField(help_text = 'write address of company')
    note = forms.CharField(help_text = 'write your note', widget = forms.Textarea, required = False)