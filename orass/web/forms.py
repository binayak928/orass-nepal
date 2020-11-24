from django import forms
from tempus_dominus.widgets import DatePicker


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
