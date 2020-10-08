from django import forms
from django.contrib.auth import password_validation, get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm as DjangoAuthenticationForm,
    UserCreationForm as DjangoUserCreationForm,
    UsernameField)
from django.utils.translation import gettext_lazy as _

# User model if needed
User = get_user_model()


class LoginForm(DjangoAuthenticationForm):
    """Customized the default AuthenticationForm
    TODO: switch from username to email for login
    """

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)


class UserCreationForm(DjangoUserCreationForm):
    """TODO: class attribute may not be given here"""
    email = forms.EmailField(
        label=_('Email'),
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email'}))
    email2 = forms.EmailField(
        label=_('Email confirmation'),
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email'}),
        help_text=_('Enter the same email as before, for verification.'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('username', 'email', 'email2', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()

        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError(
                _('The two email fields didn’t match.'),
                code='invalid',
            )
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                _('A user with that email already exists.'),
                code='invalid')
        return cleaned_data
