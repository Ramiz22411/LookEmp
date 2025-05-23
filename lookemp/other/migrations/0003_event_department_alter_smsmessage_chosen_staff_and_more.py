# Generated by Django 5.1.4 on 2025-01-28 05:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_company_balance_alter_company_created_at_and_more'),
        ('department', '0003_alter_department_weekend_days_and_more'),
        ('other', '0002_alter_event_bonus_salary_alter_event_end_date_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='department.department', verbose_name='Отдел'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='smsmessage',
            name='chosen_staff',
            field=models.ManyToManyField(related_name='chosen_staff', to='department.staff', verbose_name='Выбрать сотрудников'),
        ),
        migrations.AlterField(
            model_name='smsmessage',
            name='task_name',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='smsmessage',
            name='text_message',
            field=models.CharField(max_length=200, verbose_name='Текст смс'),
        ),
        migrations.AlterField(
            model_name='smsmessage',
            name='time_send',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время отправки'),
        ),
        migrations.AddConstraint(
            model_name='smsmessage',
            constraint=models.UniqueConstraint(fields=('task_name', 'company'), name='unique_sms_message'),
        ),
        migrations.AddConstraint(
            model_name='vocation',
            constraint=models.UniqueConstraint(fields=('company', 'start_date', 'end_date'), name='unique_vacation'),
        ),
    ]
