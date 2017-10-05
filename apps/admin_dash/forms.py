from django import forms
from django.forms import extras
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

def validate_password(password, password_confirm):
    if len(password) < 5:
        raise ValidationError(
            _('%(password) is less than 5 characters.'),
            code = 'invalid'
        )

def update_validation(first_name):
    if len(first_name) < 2:
        raise ValidationError(
            _('%(first_name) must be greater than 2 characters.'),
            params={'first_name': first_name},
        )

class Update(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, required=True)
    last_name = forms.CharField(label='Last Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)