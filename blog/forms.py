from django import forms

from .models import *


class PostForms(forms.ModelForm):

    class Meta:
        model=Post
        fields=('title','text',)