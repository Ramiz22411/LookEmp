from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('system_admin', 'Администратор (системы)'),
        ("system_manager", "Менеджер (Система)"),
        ("admin_company", "Администратор (Компании)"),
        ("manager_company", "Менеджер (Компании)"),
        ('tech_support', "Техподержка (Система)")
    ]

    email = models.EmailField(verbose_name="Email", max_length=254, unique=True)
    roles = models.CharField(
        max_length=100,
        choices=ROLE_CHOICES
    )
    company = models.ForeignKey("company.Company",
                                on_delete=models.CASCADE,
                                related_name='custom_users',
                                null=True, blank=True)