import datetime  # for checking renewal date range.

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class AddMemberForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=17)
    role = forms.ChoiceField(widget=forms.RadioSelect, choices=[("RG","Regular"), ("AD", "Admin")])
