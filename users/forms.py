from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "phone",
            "address_1",
            "address_2",
            "id_no",
            "admission_no",
            "country",
            "county",
            "sub_county",
            "location",
            "gender",
            )


class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
