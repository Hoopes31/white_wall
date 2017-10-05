from django import forms
from .models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    username=forms.CharField(min_length=3, widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'u-full-width'}), label='')
    first_name=forms.CharField(min_length=3, widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'u-full-width'}), label='')
    last_name=forms.CharField(min_length=3, widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class':'u-full-width'}), label='')
    email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email', 'class':'u-full-width'}), label='')
    password=forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'u-full-width'}), label='')
    confirm_password=forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'placeholder':'Password Confirm', 'class':'u-full-width'}), label='')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        email = cleaned_data.get('email')

        if password != confirm_password:
            raise forms.ValidationError(
                {'confirm_password': ['Passwords must match!',]}
            )
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                {'email': ['Email address must be unique.',]}
            )

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'u-full-width'}), label='')
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'u-full-width'}), label='')