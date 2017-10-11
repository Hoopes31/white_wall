from django import forms
from .models import *

class AddAnnotation(forms.Form):
    QUESTION = 'Question'
    TRANSLATION = 'Translation'
    ANNOTATION_CHOICES = (
        (QUESTION, 'Question'),
        (TRANSLATION, 'Translation')
    )

    subject=forms.CharField(min_length=3, widget=forms.TextInput(attrs={'placeholder':'Quoted Text', 'class':'u-full-width'}), label='')
    body=forms.CharField(min_length=3, widget=forms.TextInput(attrs={'placeholder':'Body', 'class':'u-full-width'}), label='')
    category=forms.ChoiceField(widget=forms.Select(attrs={'placeholder':'Response Type', 'class':'u-full-width'}), choices=ANNOTATION_CHOICES, label='')

class AddComment(forms.Form):
    
    body=forms.CharField(min_length=3, widget=forms.TextInput(attrs={'placeholder':'Response', 'class':'u-full-width'}), label='')