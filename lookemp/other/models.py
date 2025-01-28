from datetime import date

from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db import models, ProgrammingError
from django.db.models import ManyToManyField


# Create your models here.

class Event(models.Model):
    ONCE = 'ONCE'
    DALLY = 'DALLY'
    WEEKDAY = 'WEEKDAY'

    REPEAT_CHOICES = (
        (ONCE, 'Один раз'),
        (DALLY, 'Каждый раз'),
        (WEEKDAY, 'Каждую неделю'),
    )

    event_name = models.CharField(max_length=100, verbose_name="Название События")
    repeat_type = models.CharField(
        max_length=100,
        choices=REPEAT_CHOICES,
        verbose_name="Тип повторения",
        blank=True,
        null=True,
    )
    repeat_day = ArrayField(
        models.IntegerField(),
        help_text='The number of days that the event repeats.',
        size=6,
        blank=True,
        null=True,
        verbose_name="Дни потвторения"
    )

    start_date_time = models.DateTimeField(default=date.today, verbose_name="Время начало события")
    end_date_time = models.DateTimeField(default=date.today, verbose_name="Время окончания события")
    bonus_salary = models.BooleanField(default=False, verbose_name="Бонус за посещения")
    lateness_penalty = models.BooleanField(default=False, verbose_name="Штраф за опоздания")
    penalty_per_min = models.IntegerField(default=0, verbose_name="Штраф в минуту")
    total_penalty = models.IntegerField(default=0, blank=True, null=True, verbose_name="Общий штраф")
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE,
                                related_name='events', blank=True, null=True)
    department = models.ForeignKey(
        'department.Department',
        on_delete=models.CASCADE,
        verbose_name="Отдел",
        related_name='events',
    )

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return self.event_name


class SmsMessage(models.Model):
    task_name = models.CharField(max_length=100, verbose_name="Заголовок")
    text_message = models.CharField(max_length=200, verbose_name="Текст смс")
    time_send = models.DateTimeField(auto_now_add=True, verbose_name="Время отправки")
    chosen_staff = ManyToManyField(
        'department.Staff',
        related_name="chosen_staff",
        verbose_name="Выбрать сотрудников"

    )
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE,
                                related_name='sms_messages', blank=True, null=True)
    sid = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['task_name', 'company'],
                name='unique_sms_message',
            )
        ]
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.task_name


class Vocation(models.Model):
    chosen_staff = models.ManyToManyField('department.Staff', related_name="staffs_to_vacation")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE,
                                related_name='vacations', blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['company', 'start_date', 'end_date'],
                name='unique_vacation',
            )
        ]
        verbose_name = "Отпуск"
        verbose_name_plural = "Отпуски"

    def __str__(self):
        return f"Сотрудники на отпуск {self.chosen_staff} даты {self.start_date} - {self.end_date}"

    def validate_date(self):
        if self.start_date == self.end_date:
            raise ValidationError("Дата Отпуска и дата окончания не должен быть одинаковым")


class AppSetting(models.Model):
    company = models.OneToOneField('company.Company', on_delete=models.CASCADE)
    total_hours_overworked = models.IntegerField(default=12)
    time_send_sms = models.IntegerField(default=2)
    allow_exit = models.IntegerField(default=2)

    class Meta:
        verbose_name_plural = "Настройки"

    @classmethod
    def load(cls, company_id):
        try:
            if not cls.objects.filter(company_id=company_id).exists():
                return cls.objects.create(company_id=company_id)
            return cls.objects.filter(company_id=company_id).first()
        except ProgrammingError:
            return None
