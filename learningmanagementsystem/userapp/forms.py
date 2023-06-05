from django.forms import ModelForm

from .models import (
    MyUser
)


class MyUserLoginForm(ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'email',
            'password'
        ]
