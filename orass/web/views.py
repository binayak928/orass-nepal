import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import DonationsDemo


# Create your views here.
# from requests import request


def home_page(request):
    context = {}
    return render(request, 'web/base.html', context)


def test_page(request):
    context = {}
    return render(request, 'web/test.html', context)


def contact_page(request):
    context = {}
    return render(request, 'web/contact.html', context)


def donor_page(request):
    all_donations = DonationsDemo.objects.all()
    context = {
        "donations": all_donations
    }
    return render(request, 'web/donor.html', context)
