from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils.translation import gettext_lazy as _


class Type(models.Model):
    CHOICES = [
        ("pr", "provider"),
        ("co", "consumer"),
    ]


# Create your CustomUserManager here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, username, type, **extra_fields):
        if not email:
            raise ValueError(_("Email must be provided"))
        if not username:
            raise ValueError(_("Username must be provided"))
        if not password:
            raise ValueError(_("Password is not provided"))
        if not type:
            raise ValueError(_("Type is not provided"))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            type=type,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self,
        email,
        password,
        username,
        type,
        **extra_fields,
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(
            email,
            password,
            username,
            type,
            **extra_fields,
        )

    def create_superuser(
        self,
        email,
        password,
        username,
        type,
        **extra_fields,
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(
            email,
            password,
            username,
            type,
            **extra_fields,
        )


# Create your User Model here.
class User(AbstractBaseUser, PermissionsMixin):
    # Abstractbaseuser has password, last_login, is_active by default

    email = models.EmailField(
        db_index=True,
        blank=False,
        unique=True,
        max_length=150,
    )
    username = models.CharField(
        unique=True,
        blank=False,
        max_length=100,
    )
    type = models.CharField(
        max_length=2,
        choices=Type.CHOICES,
        default="co",
    )

    is_staff = models.BooleanField(
        _("staff"), default=True
    )  # must needed, otherwise you won't be able to loginto django-admin.
    is_active = models.BooleanField(
        _("active"), default=True
    )  # must needed, otherwise you won't be able to loginto django-admin.
    is_superuser = models.BooleanField(
        _("superuser"), default=False
    )  # this field we inherit from PermissionsMixin.

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "email",
        "type",
    ]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        unique_together = (
            "username",
            "email",
        )
