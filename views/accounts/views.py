from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import reverse

# class LoginView(FormView):
# GET - отдает форму с запросом логина и пароля
# POST - генерирует сессию: отдавая ее пользователю


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_field_name = 'next'  # default
    extra_context = {'key': 'value'}
    authentication_form = AuthenticationForm  # default


class UserLogoutView(LogoutView):

    template_name = 'accounts/logout.html'
    # next_page = '/'
    redirect_field_name = 'next'
    extra_context = {}


# PasswordChangeView(FormView)
class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    succes_url = reverse('password_change_done')
    extra_context = {}
    # form_class = PasswordChangeForm default


# PasswordChangeDoneView(TemplateView)
class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'
    extra_context = {}  # title


















