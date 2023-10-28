from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Name")
    second_name = forms.CharField(label="Lastname")

    class Meta:
        model = User
        fields = ("username",
                  "first_name", # опционально
                  "last_name", # опционально
                  "email",
                  "password1",
                  "password2", )
