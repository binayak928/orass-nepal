from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker


class DonorRegistrationForm(forms.Form):
    name = forms.CharField(label='Name')
    date = forms.DateField(
        widget=DatePicker(
            options={
                'ignoreReadonly': True,
            },
            attrs={
                'append': 'fa fa-calendar',
            }
        )
    )
    amt = forms.CharField(label='Amount')


class BlogCreationForm(forms.Form):
    author = forms.CharField(label='Author Name', required=True)
    post_date = forms.DateField(
        widget=DatePicker(
            options={
                'ignoreReadonly': True,
            },
            attrs={
                'append': 'fa fa-calendar',
            }
        )
    )
    title = forms.CharField(label='Blog Title', required=True)
    category = forms.CharField(label='Blog Category', required=True)
    body = forms.CharField(label='Blog Title', required=True, widget=forms.Textarea)
    picture = forms.ImageField(label='Blog Image:')


class EventCreationForm(forms.Form):
    date = forms.DateField(label='Event Date',
                           widget=DatePicker(
                               options={
                                   'ignoreReadonly': True,
                               },
                               attrs={
                                   'append': 'fa fa-calendar',
                               }
                           )
                           )
    start = forms.TimeField(
        input_formats=['%I:%M %p'],
        widget=TimePicker(
            options={
                'format': 'LT',
                'ignoreReadonly': True,
            },
            attrs={
                'append': 'fa fa-clock'
            }
        )
    )
    end = forms.TimeField(
        input_formats=['%I:%M %p'],
        widget=TimePicker(
            options={
                'format': 'LT',
                'ignoreReadonly': True,
            },
            attrs={
                'append': 'fa fa-clock'
            }
        )
    )
    title = forms.CharField(label='Event Title', required=True)
    description = forms.CharField(label='Event Description', required=True, widget=forms.Textarea)
    address_street = forms.CharField(label='Street', required=True)
    address_city = forms.CharField(label='City', required=True)
    address_country = forms.CharField(label='Country:', required=True)
    organizer = forms.CharField(label='Organizer Name:', required=True)
    phone = forms.CharField(label='Phone:', required=True)
    email = forms.CharField(label='Email address:', required=True)
    picture = forms.ImageField(label='Event Banner Image:')
