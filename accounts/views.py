from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin)
from django.contrib.auth.views import (
    FormView,
    LoginView as DjangoLoginView, LogoutView as DjangoLogoutView,
    PasswordResetView as DjangoPasswordResetView)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from core.views import HomeView
from .forms import LoginForm, UserCreationForm

# User model if needed
User = get_user_model()


class LoginView(DjangoLoginView):
    """Expecially LoginForm is customized."""
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Login')
        context['title_alt'] = _('Accounts')
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('User Profile')
        context['title_alt'] = _('Accounts')
        return context


class LogoutView(DjangoLogoutView):
    """Logout redirects to home."""
    pass


class PasswordResetView(DjangoPasswordResetView):
    """TODO: implement"""


class RegisterView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Registration')
        context['title_alt'] = _('Accounts')
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
