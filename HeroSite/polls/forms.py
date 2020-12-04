from .models import Superhero
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SuperheroAddForm(forms.ModelForm):
    class Meta:
        model = Superhero
        fields = ["name", "description", "birthyear", "deathyear", "img"]


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
