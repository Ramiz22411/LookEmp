from django.forms import ModelForm

from .models import PaymentTransaction, BonusTransaction


class PaymentTransactionAtomicForm(ModelForm):
    class Meta:
        model = PaymentTransaction
        fields = ('quantity', 'comment', 'staff', 'company')


class BonusPaymentTransactionAtomicForm(ModelForm):
    class Meta:
        model = BonusTransaction
        fields = ('quantity', 'comment', 'staff', 'company')
