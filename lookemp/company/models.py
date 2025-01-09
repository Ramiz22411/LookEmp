from datetime import date

from django.db import models

# Create your models here.

class Company(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('blocked', 'Blocked'),
        ('on_subscription', 'On_subscription'),
    )

    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    subscription_end = models.DateTimeField(null=True, blank=True)

    def is_active(self):
        return self.status == 'active' and self.subscription_end >= date.today()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'