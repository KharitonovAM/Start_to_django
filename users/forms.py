from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from catalog.forms import StyleFormMixim

from users.models import User


class UserRegisterForm(StyleFormMixim, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("email", "phone", "avatar", "country")
