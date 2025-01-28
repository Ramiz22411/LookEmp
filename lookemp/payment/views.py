from django.db import transaction
from django.views.generic import CreateView, ListView
from .models import BonusTransaction, PaymentTransaction
from .forms import PaymentTransactionAtomicForm, BonusPaymentTransactionAtomicForm


# Create your views here.

class LIstPaymentTransactionView(ListView):
    model = PaymentTransaction
    template_name = ''
    context_object_name = 'transactions'


class CreatePaymentTransactionAtomic(CreateView):
    form_class = PaymentTransactionAtomicForm
    template_name = 'payments/payment.html'

    def form_valid(self, form):
        with transaction.atomic():
            staff = form.cleaned_data['staff']
            quantity = form.cleaned_data['quantity']

            if staff.balance < quantity:
                form.add_error('quantity', 'Недостаточно средств на балансе')
                return super().form_invalid(form)

            staff.balance -= quantity
            staff.save()
            return super().form_valid(form)


class ListBonusTransactionView(ListView):
    model = BonusTransaction
    template_name = ''
    context_object_name = 'bonuses'


class CreatePaymentBonusAtomic(CreateView):
    form_class = BonusPaymentTransactionAtomicForm
    template_name = 'payments/bonus.html'

    def form_valid(self, form):
        with transaction.atomic():
            staff = form.cleaned_data['staff']
            quantity = form.cleaned_data['quantity']

            staff.balance += quantity
            return super().form_valid(form)
