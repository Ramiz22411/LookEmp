from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

class Department(models.Model):
    name_of_department = models.CharField(max_length=100)
    start_work_time = models.TimeField(verbose_name="Начало рабочего дня", blank=True, null=True)
    allowed_lateness = models.IntegerField(verbose_name="Фора опоздания в минутах")
    end_work_time = models.TimeField(verbose_name="Конец рабочего дня", blank=True, null=True)
    lateness_penalty = models.BooleanField(verbose_name="Штраф за опоздания")
    lateness_penalty_per_min = models.IntegerField(verbose_name="Штраф за опоздания в мин")
    sum_penalty = models.IntegerField(verbose_name="Сумма штрафа", default=0)
    close_attendance = models.BooleanField(verbose_name="Закрывать посешения по умолчанию", default=True)
    lunch_time = models.TimeField(verbose_name="Время обеда", blank=True, null=True)
    allowed_lunch_time = models.IntegerField(verbose_name="Фора за посешение обеда")
    end_lunch = models.TimeField(verbose_name="Конец Обеда", blank=True, null=True)
    salary_for_lunch = models.BooleanField(verbose_name="Начисления зп за обед")
    weekend_days = ArrayField(
        models.IntegerField(),
        size=6,
        blank=True,
        null=True,
    )
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE,
                                related_name="departments", blank=True, null=True)

    def calculate_sum_penalty(self, lateness):
        if lateness > self.allowed_lateness:
            return 0
        extra_min = lateness - self.allowed_lateness
        return int(self.lateness_penalty_per_min * extra_min)

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    def __str__(self):
        return self.name_of_department


class Staff(models.Model):
    name = models.CharField(verbose_name="Имя(на англ)", max_length=100)
    surname = models.CharField(verbose_name="Фамилия(на англ)", max_length=100)
    is_active = models.BooleanField(verbose_name="Статус", default=False, blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Дата Рождения")
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=20, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="departments")
    salary_stratage = ArrayField(
        models.IntegerField(),
        size=2,
        verbose_name="Стратегия зп(месяц, час)",
    )
    balance = models.IntegerField(verbose_name="Зарплата", default=0)
    is_flexible_schedule = models.BooleanField(verbose_name="Персональный график сотрудника",
                                               default=False, blank=True, null=True)
    start_time = models.TimeField(verbose_name="начало работы", blank=True, null=True)
    end_time = models.TimeField(verbose_name="конец работы", blank=True, null=True)
    company = models.ForeignKey(
        'company.Company',
        on_delete=models.CASCADE,
        related_name="employees",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f'{self.name} - {self.surname}'
