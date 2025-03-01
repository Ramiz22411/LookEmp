from django import forms
from django.forms.widgets import CheckboxSelectMultiple, RadioSelect

from .models import Staff, Department


class StaffForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        input_formats=['%d-%m-%Y', '%m-%d-%Y', '%Y-%m-%d'],
    )

    class Meta:
        model = Staff
        fields = [
            'name', 'surname',
            'date_of_birth', 'phone_number', 'salary_strategy',
            "is_flexible_schedule",
            "balance",
            "start_time",
            "end_time",
            "department",
        ]


class DepartmentForm(forms.ModelForm):
    weekend_days = forms.MultipleChoiceField(
        required=False,
        choices=[
            ("0", "ПН"), ("1", "ВТ"), ("2", "СР"),
            ("3", "ЧТ"), ("4", "ПТ"), ("5", "СБ"), ("6", "ВС")
        ],
        widget=CheckboxSelectMultiple
    )

    class Meta:
        model = Department
        fields = [
            'name_of_department',
            'start_work_time',
            'allowed_lateness',
            'end_work_time',
            'lateness_penalty',
            'lateness_penalty_per_min',
            'sum_penalty',
            'close_attendance',
            'lunch_time',
            'allowed_lunch_time',
            'end_lunch',
            'salary_for_lunch',
            'weekend_days'
        ]
