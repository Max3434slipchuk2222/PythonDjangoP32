from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse_lazy

from mysite import settings
from .forms import (
    CustomUserCreationForm,
    CustomUserLoginForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm,
)
import os

from .utils import compress_image, save_custom_image


# Create your views here.
def register(request):
    if request.method == 'POST':
        # print("---Зберігаємо дані користувача---")
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                if 'email' in form.cleaned_data:
                    user.username = form.cleaned_data['email']
                if 'image' in request.FILES:
                    image = request.FILES.get("image")
                    user.image_small = save_custom_image(image, size=(300,300), folder="small")
                    user.image_medium = save_custom_image(image, size=(800,800), folder="medium")
                    user.image_large = save_custom_image(image, size=(1200,1200), folder="large")
                user.save()
                login(request, user)
                return redirect('homepage')
            except Exception as e:
                messages.error(request, f"Щось пішло не так: {str(e)}")
        else:
            messages.success(request, 'Виправте помилки у формі')
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.error(request, 'Невірний логін або пароль')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('homepage')

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'password_reset.html'
    email_template_name = 'emails/password_reset_email.html'  # тіло листа (plain text)
    subject_template_name = 'emails/password_reset_subject.txt'  # тема листа
    success_url = reverse_lazy('users:password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'