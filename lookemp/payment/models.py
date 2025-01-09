from django.db import models

# Create your models here.

class PaymentTransaction(models.Model):
    staff = models.ForeignKey('department.Staff', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Сумма списания")
    comment = models.TextField(verbose_name="Коментарий", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата выдвчи")
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE,
                                related_name="payment_transactions", blank=True, null=True)

    class Meta:
        verbose_name = "Списание"
        verbose_name_plural = "Списания"

    def __str__(self):
        return f"Transaction {self.staff.name} - {self.quantity}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class BonusTransaction(models.Model):
    staff = models.ForeignKey('department.Staff', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Сумма начисления")
    comment = models.TextField(verbose_name="Кометарии", blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата получения бонуса")
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE,
                                related_name="bonus_transactions", blank=True, null=True)

    class Meta:
        verbose_name = "Бонус"
        verbose_name_plural = "Бонусы"

    def __str__(self):
        return f"Transaction {self.staff.name} - {self.quantity}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)