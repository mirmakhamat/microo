from django import forms
from .models import CallBack, Subscription


class CallBackForm(forms.ModelForm):
    class Meta:
        model = CallBack
        fields = ('name', 'email', 'phone_number', 'message')


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('email',)
