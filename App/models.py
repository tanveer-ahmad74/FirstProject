from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class SoftDelete(models.Model):
    is_delete = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_delete = True
        self.save()

    def restore(self):
        self.is_delete = False
        self.save()

    class Meta:
        abstract = True


class Colors(SoftDelete):
    color_name = models.CharField(max_length=30)
    hex_color_code = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.color_name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


# An abstract model is a base class in which you define fields you want to include in all child models.
# Django doesn't create any database table for abstract models


class User(AbstractUser, SoftDelete):
    email = models.EmailField(unique=True)
    address = models.TextField(null=True, blank=True)
    mobile_number = models.CharField(max_length=13, null=True, blank=True)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE, null=True, blank=True)

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Users'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
