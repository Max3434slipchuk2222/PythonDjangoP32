from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Електронна пошта",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        label="Ім'я",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Вкажіть ім'я"})
    )
    last_name = forms.CharField(
        label="Прізвище",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    image = forms.ImageField(
        label="Зображення",
        required=True,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Пароль",
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Повторіть пароль",
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'image', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Дана пошта вже зареєстрована")
        return email

    def clean_password2(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Паролі не співпадають.")
        return p2

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логін (email)",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Електронна пошта",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your@email.com',
            'autocomplete': 'email',
        })
    )

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="Новий пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label="Підтвердіть новий пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )