from django.urls import path
from . import views

urlpatterns = [
    path('event', views.EventView.as_view(), name='event'),
    path('event/list', views.EventListView.as_view(), name='event-list'),
    path('sms', views.SmsMessageView.as_view(), name='sms_message'),
    path('sms_list', views.SmsMessageListView.as_view(), name='sms_message-list'),
    path('vocation', views.VocationView.as_view(), name='vocation'),
    path('vocation/list', views.VocationListView.as_view(), name='vocation-list'),

]
