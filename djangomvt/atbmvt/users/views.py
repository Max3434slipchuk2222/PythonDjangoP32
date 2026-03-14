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

from .forms import (
    CustomUserCreationForm,
    CustomUserLoginForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm,
)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.username = form.cleaned_data['email']  # email як логін
                if 'image' in request.FILES:
                    image = request.FILES['image']
                    user.image_small = image
                    user.image_medium = image
                    user.image_large = image
                user.save()
                login(request, user)
                return redirect('homepage')
            except Exception as e:
                messages.error(request, f"Щось пішло не так: {str(e)}")
        else:
            messages.error(request, 'Виправте помилки у формі')  # було success — виправлено
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


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