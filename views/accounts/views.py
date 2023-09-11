from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import reverse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.apps import apps
from django.http import HttpResponseRedirect


# class LoginView(FormView):
# GET - отдает форму с запросом логина и пароля
# POST - генерирует сессию: отдавая ее пользователю


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('main_page')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        Author = apps.get_model('views_app', 'Author')
        self.object = form.save()
        new_author = Author(name=self.object.username, user=self.object, bio='bio', email=self.object.email)
        new_author.save()
        return HttpResponseRedirect(self.get_success_url())


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
    succes_url = reverse_lazy('password_change_done')
    extra_context = {}
    # form_class = PasswordChangeForm default


# PasswordChangeDoneView(TemplateView)
class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'
    extra_context = {}  # title


















