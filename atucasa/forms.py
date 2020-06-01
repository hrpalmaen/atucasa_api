from django import forms
from .models import AuthUser


class PostForm(forms.ModelForm):

    class Meta:
        model = AuthUser
        fields = ['password','username','first_name']