from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Visit(models.Model):
    currently_date = models.DateTimeField(verbose_name="Вход на данный момент")
    currently_date_exit = models.DateTimeField(verbose_name="Выход на данный момент")
    enter_date = models.DateTimeField(verbose_name="Дата входа")
    exit_date = models.DateTimeField(verbose_name="Дата выхода")
    default_work_star_time = models.DateTimeField(
        verbose_name="Время работы по умолчанию",
        null=True,
        blank=True
    )
    default_work_end_time = models.DateTimeField(
        verbose_name="Конец рабочего дня по умолчанию",
        null=True,
        blank=True
    )
    total_minutes = models.DecimalField(verbose_name="Общее время в минутах", max_digits=5, decimal_places=2)
    total_minutes_late = models.DecimalField(verbose_name="Общее время опоздание в минутах", max_digits=5,
                                             decimal_places=2)
    late = models.BooleanField(verbose_name="Опоздание", default=False)
    visit_default_closed_by_system = models.BooleanField(verbose_name="Закрыто по умолчанию", default=False)
    manual_created = models.BooleanField(verbose_name="Создано вручную", default=False)
    manual_updated = models.BooleanField(verbose_name="Обновлено вручную", default=False)
    user = models.ForeignKey(User, related_name="visits", on_delete=models.CASCADE)
    staff = models.ForeignKey('department.Staff', related_name="staff_visits", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Визит"
        verbose_name_plural = "Визиты"
        ordering = ["-currently_date"]

    def __str__(self):
        return f"{self.user} - {self.currently_date}"