from django.views.generic import CreateView, ListView


from .forms import SmsMessageForm
from .models import Event, SmsMessage, AppSetting, Vocation


# Create your views here.

class EventView(CreateView):
    model = Event
    fields = '__all__'
    template_name = 'others/event/create_event.html'
    success_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['week_days'] = [
            (0, "Понедельник"),
            (1, "Вторник"),
            (2, "Среда"),
            (3, "Четверг"),
            (4, "Пятница"),
            (5, "Суббота"),
            (6, "Воскресенье")
        ]
        return context

    def form_valid(self, form):
        return super().form_valid(form)


class EventListView(ListView):
    model = Event
    template_name = 'others/event/event_list.html'
    context_object_name = 'events'


class SmsMessageView(CreateView):
    model = SmsMessage
    template_name = 'others/sms/sms_create.html'
    form_class = SmsMessageForm
    success_url = ''

    def form_valid(self, form):
        return super().form_valid(form)


class SmsMessageListView(ListView):
    model = SmsMessage
    context_object_name = 'messages'
    template_name = 'others/sms/sms_create.html'


class VocationView(CreateView):
    model = Vocation
    fields = '__all__'
    template_name = ''
    success_url = ''

    def form_valid(self, form):
        return super().form_valid(form)


class VocationListView(ListView):
    model = Vocation
    context_object_name = 'vocations'
    template_name = ''
