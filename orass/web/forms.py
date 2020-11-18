from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from .models import DonationsDemo


class DonorRegistrationForm(forms.Form):
    name = forms.CharField(label='Name', required=True)
    date = forms.DateField(
        widget=DatePicker(
            options={
                'ignoreReadonly': True,
            },
            attrs={
                'append': 'fa-fa-calendar',
            }
        )
    )
    amt = forms.CharField(label='Amount', required=True)
