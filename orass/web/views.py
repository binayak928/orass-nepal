import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# from requests import request


def home_page(request):
    context = {}
    return render(request, 'web/base.html', context)
