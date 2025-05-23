from datetime import date

from django.db import models

# Create your models here.

class Company(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('blocked', 'Blocked'),
        ('on_subscription', 'On_subscription'),
    )

    name = models.CharField(max_length=100, verbose_name='Имя компании')
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Баланс")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время Создания")
    subscription_end = models.DateTimeField(null=True, blank=True, verbose_name='Окончания подписки')

    def is_active(self):
        return self.status == 'active' and self.subscription_end >= date.today()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'