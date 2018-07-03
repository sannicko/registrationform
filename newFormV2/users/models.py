from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.db.models import signals
from django.conf import settings

class UserManager(BaseUserManager):

    def _private_Function(self, email, password, is_superuser, is_active, **extra_fields):
        """Creates and saves a User with the given username, email and password.
            """
        now = timezone.now()
        if not email:
            raise ValueError(
                _('Email is required to create user'))
        email = self.normalize_email(email)
        user = self.model(email=email, is_active=is_active,is_superuser=is_superuser, last_login=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._private_Function(email, password, False, False, False, user_role=user_role, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._private_Function(email, password, is_superuser=True,is_active=True, **extra_fields)


class ApplicationUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        verbose_name=_("First Name"), max_length=50, null=True, blank=True)
    
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=50)
    
    email = models.EmailField(verbose_name=_("Email"), unique=False,null=True,blank=True)

    phoneNumber = models.CharField(verbose_name=_("Phone Number"),max_length=17, blank=True,null=True,unique=True)

    is_active = models.BooleanField(_('active'), default=True, help_text=_('Designates whether this user should be treated as ' 'active. '
                                                                           'Unselect this instead of deleting accounts.'))


    objects = UserManager()
    USERNAME_FIELD = 'phoneNumber'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        name = '%s %s' % self.first_name, self.last_name
        return name

    def get_short_name(self):
        return '%s' % (self.first_name)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
