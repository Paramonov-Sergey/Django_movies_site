from django import forms
from.models import Reviews,Rating
from django.core.exceptions import ValidationError
import re

class ReviewsForm(forms.ModelForm):
    class Meta:
        model=Reviews
        fields=['email','name','text']


    def clean_name(self):
        new_name=self.cleaned_data['name']
        if new_name=='create':
           raise ValidationError('Попробуйте еще раз ')



class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        fields=['star']