from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.views.generic import CreateView, ListView, UpdateView
from .models import BonusTransaction, PaymentTransaction
from .forms import PaymentTransactionAtomicForm, BonusPaymentTransactionAtomicForm


# Create your views here.

class ListTransactionView(LoginRequiredMixin, ListView):
    model = PaymentTransaction
    template_name = 'payments/list_transaction.html'
    context_object_name = 'payments'


class UpdateTransactionView(LoginRequiredMixin, UpdateView):
    template_name = 'payments/update_transaction.html'
    form_class = PaymentTransactionAtomicForm
    model = PaymentTransaction
    context_object_name = 'payment'
    success_url = '/transaction_list/'

    def form_valid(self, form):
        user_company = self.request.user.company
        new_staff = form.cleaned_data['staff']

        if new_staff.company != user_company:
            form.add_error('staff', 'Сотрудник не принадлежит вашей компании')
            return super().form_invalid(form)

        old_transaction = self.get_object()
        old_quantity = old_transaction.quantity
        old_staff = old_transaction.staff

        new_quantity = form.cleaned_data['quantity']

        with transaction.atomic():
            if new_staff == old_staff:
                available_balance = new_staff.balance + old_quantity
                if available_balance < new_quantity:
                    form.add_error('quantity', 'Недостаточно средств на балансе')
                    return self.form_invalid(form)
                new_staff.balance = available_balance - new_quantity
                new_staff.save()
            else:
                old_staff.balance += old_quantity
                old_staff.save()

                if new_staff.balance < new_quantity:
                    form.add_error('quantity', 'Недостаточно средств на балансе')
                    return self.form_invalid(form)
                new_staff.balance -= new_quantity
                new_staff.save()

        return super().form_valid(form)


class CreatePaymentTransactionAtomic(CreateView):
    form_class = PaymentTransactionAtomicForm
    template_name = 'payments/payment.html'
    success_url = '/department/staff_list'

    def form_valid(self, form):
        user_company = self.request.user.company
        staff = form.cleaned_data['staff']

        if staff.company != user_company:
            form.add_error('staff', 'Сотрудник не принадлежит вашей компании')
            return super().form_invalid(form)

        with transaction.atomic():
            quantity = form.cleaned_data['quantity']

            if staff.balance < quantity:
                form.add_error('quantity', 'Недостаточно средств на балансе')
                return super().form_invalid(form)

            staff.balance -= quantity
            staff.save()
        return super().form_valid(form)


class ListBonusPaymentView(ListView):
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
