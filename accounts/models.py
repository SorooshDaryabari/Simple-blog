from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email_unique_code = models.CharField(max_length=260)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        if self.first_name != "" and self.last_name != "":
            return self.get_full_name()
        else:
            return self.username


class Profile(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        verbose_name=_("Profile"),
        on_delete=models.CASCADE
    )
    account_id = models.CharField(unique=True, max_length=255, verbose_name=_("Account id"))
    profile_image = models.ImageField(
        upload_to="images/profile_images/",
        verbose_name=_("Profile image"),
        null=True,
        blank=True,
    )
    phone_number = models.DecimalField(
        null=True,
        blank=True,
        max_digits=11,
        verbose_name=_("Phone number"),
        decimal_places=0,
    )
    about = models.TextField(verbose_name=_("About"), null=True, blank=True, )
    is_author = models.BooleanField(default=False)
    resume = models.FileField(
        verbose_name=_("Resume"),
        upload_to="resumes/user_resumes/",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.account_id


class Follower(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name=_("Profile"))
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="following",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    follower = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="followers",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        account_id = self.profile.account_id
        return account_id
