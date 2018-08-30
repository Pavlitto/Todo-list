from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm


from todos.models import CustomUser, Organisation


class CustomAuthenticationForm(AuthenticationForm):
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        comp = self.cleaned_data.get('comp')

        try:
            self.user_cache = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            forms.ValidationError('{} user not found'.format(email))
        try:
            org = Organisation.objects.get(name__iexact=comp)
        except Organisation.DoesNotExist:
            forms.ValidationError('{} Organisation not found'.format(comp))

        if not self.user_cache.comp.filter(pk=org.pk).exists():
            forms.ValidationError("User doesn't exists in Organisation")

        self.confirm_login_allowed(self.user_cache)

        # здесь кастомный бэк должен запихать ид организации в сессию
        self.user_cache = authenticate(self.request, username=email, password=password, organization=org)

        return self.cleaned_data
