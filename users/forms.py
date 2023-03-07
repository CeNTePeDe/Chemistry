from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from users.models import User


class UserLoggingForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите пороль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Введите email'}))
    password1 = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Введите пароль еще раз'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    image_field = forms.ImageField(widget=forms.ImageField(),  required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите никнейм'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имейл'}))
    education = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите образование'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image_field', 'username', 'email', 'education')
