from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    address = models.TextField(blank=True, verbose_name="Adresse")

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",
        related_query_name="user",
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",
        related_query_name="user",
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.'
    )
