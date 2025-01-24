from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'roles', 'company', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        return user
