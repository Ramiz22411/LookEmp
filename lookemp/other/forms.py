from django import forms
from .models import SmsMessage


class SmsMessageForm(forms.ModelForm):
    class Meta:
        model = SmsMessage
        fields = '__all__'
        widgets = {
            'chosen_staff': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
        }
