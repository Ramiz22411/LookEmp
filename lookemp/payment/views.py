from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from department.models import Staff
from .models import BonusTransaction, PaymentTransaction
from .forms import PaymentTransactionAtomicForm, BonusPaymentTransactionAtomicForm


# Create your views here.

class ListTransactionView(LoginRequiredMixin, ListView):
    model = PaymentTransaction
    template_name = 'payments/list_transaction.html'
    context_object_name = 'payments'

    def queryset(self):
        return PaymentTransaction.objects.filter(company=self.request.user.company)


class UpdateTransactionView(LoginRequiredMixin, UpdateView):
    template_name = 'payments/update_transaction.html'
    form_class = PaymentTransactionAtomicForm
    model = PaymentTransaction
    context_object_name = 'payment'
    success_url = '/payment/transaction_list/'

    def form_valid(self, form):
        user_company = self.request.user.company
        form.instance.company = user_company
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


class CreatePaymentTransactionAtomic(LoginRequiredMixin, CreateView):
    form_class = PaymentTransactionAtomicForm
    template_name = 'payments/payment.html'
    success_url = '/department/staff_list'

    def form_valid(self, form):
        user_company = self.request.user.company
        form.instance.company = user_company
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

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user = self.request.user
        if hasattr(user, 'company'):
            form.fields['staff'].queryset = Staff.objects.filter(company=user.company)
        return form


class DeleteTransactionView(LoginRequiredMixin, DeleteView):
    success_url = '/department/staff_list'
    model = PaymentTransaction

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        with transaction.atomic():
            staff = self.object.staff
            staff.balance += self.object.quantity
            staff.save()
            return super().delete(request, *args, **kwargs)


class ListBonusPaymentView(LoginRequiredMixin, ListView):
    model = BonusTransaction
    template_name = 'payments/list_bonus.html'
    context_object_name = 'bonuses'

    def queryset(self):
        return BonusTransaction.objects.filter(company=self.request.user.company)


class CreatePaymentBonusAtomic(LoginRequiredMixin, CreateView):
    form_class = BonusPaymentTransactionAtomicForm
    template_name = 'payments/bonus.html'
    success_url = '/department/staff_list'

    def form_valid(self, form):
        user_company = self.request.user.company
        form.instance.company = user_company
        staff = form.cleaned_data['staff']

        if staff.company != user_company:
            form.add_error('staff', 'Сотрудник не принадлежит вашей компании')
            return super().form_invalid(form)

        with transaction.atomic():
            quantity = form.cleaned_data['quantity']
            staff.balance += quantity
            staff.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user = self.request.user
        if hasattr(user, 'company'):
            form.fields['staff'].queryset = Staff.objects.filter(company=user.company)
        return form


class UpdateBonusTransactionView(LoginRequiredMixin, UpdateView):
    template_name = 'payments/update_bonus.html'
    form_class = BonusPaymentTransactionAtomicForm
    model = BonusTransaction
    context_object_name = 'bonus'
    success_url = '/payment/bonus_list/'

    def form_valid(self, form):
        user_company = self.request.user.company
        form.instance.company = user_company
        new_staff = form.cleaned_data['staff']

        if new_staff.company != user_company:
            form.add_error('staff', 'Сотрудник не принадлежит вашей компании')
            return super().form_valid(form)

        old_bonus = self.get_object()
        old_quantity = old_bonus.quantity
        old_staff = old_bonus.staff

        new_quantity = form.cleaned_data['quantity']

        with transaction.atomic():
            if new_staff == old_staff:
                new_staff.balance = new_staff.balance - old_quantity + new_quantity
                new_staff.save()
            else:
                old_staff.balance = old_staff.balance - old_quantity
                old_staff.save()

                new_staff.balance = new_staff.balance + new_quantity
                new_staff.save()

        return super().form_valid(form)


class DeleteBonusTransactionView(LoginRequiredMixin, DeleteView):
    model = BonusTransaction
    success_url = '/department/staff_list'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        with transaction.atomic():
            staff = self.object.staff
            staff.balance -= self.object.quantity
            staff.save()
            return super().delete(request, *args, **kwargs)


