from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Permission
from django.utils.translation import ugettext_lazy as _

from .managers.CustomUserManager import CustomUserManager


class Organisation(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        """A string representation of the model."""
        return self.name


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'),
                              max_length=254, unique=True)
    first_name = models.CharField(_('first name'),
                                  max_length=30, blank=True)
    last_name = models.CharField(_('last name'),
                                 max_length=30, blank=True)

    is_staff = models.BooleanField(_('staff status'),
                                   default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    comp = models.ManyToManyField(
        Organisation, related_name='company')
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_username(self):
        """Return the identifying username for this User"""
        return getattr(self, self.USERNAME_FIELD)

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


class Todo(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        """A string representation of the model."""
        return self.title


