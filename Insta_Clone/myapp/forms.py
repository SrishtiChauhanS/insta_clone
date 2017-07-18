from django import forms
from models import UserModel


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']