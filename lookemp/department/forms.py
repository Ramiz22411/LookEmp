from django import forms

from .models import Staff


class StaffForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        input_formats=['%d-%m-%Y', '%m-%d-%Y', '%Y-%m-%d'],
    )

    class Meta:
        model = Staff
        fields = [
            'name', 'surname',
            'date_of_birth', 'phone_number', 'salary_stratage',
            "is_flexible_schedule",
            "balance",
            "start_time",
            "end_time",
            "department",
        ]
