import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView
from .forms import DonorRegistrationForm
from .models import DonationsDemo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


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


def faq_page(request):
    context = {}
    return render(request, 'web/faq.html', context)


def about(request):
    context = {}
    return render(request, 'web/aboutus.html', context)


def team_page(request):
    context = {}
    return render(request, 'web/team.html', context)


def blog_page(request):
    context = {}
    return render(request, 'web/blog.html', context)


def project_page(request):
    context = {}
    return render(request, 'web/project.html', context)


def event_page(request):
    context={}
    return render(request, 'web/event.html', context)


def detail_page(request):
    context={}
    return render(request, 'web/registration.html', context)


class Login(auth_views.LoginView):
    template_name = 'registration/login.html'


@login_required(login_url="/staff")
def staff_home(request):
    context = {}
    return render(request, 'staff/index.html', context)


class PasswordChange(auth_views.PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('web:change-password-completed')


@login_required(login_url="/staff")
def donor_registration_view(request):
    if request.method == "POST":
        form = DonorRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_appointment = DonationsDemo(name=data['name'],
                                            date=data['date'],
                                            amt=data['amt'],
                                            )
            new_appointment.save()
            return redirect('web:view-donor')
    else:
        form = DonorRegistrationForm()
    return render(request, 'staff/donor_registration.html', {'form': form})


@login_required(login_url="/staff")
def password_change_complete(request):
    return render(request, 'registration/change_password_completed.html')


class DonorList(ListView):
    model = DonationsDemo
    template_name = 'staff/view_donor.html'


class ViewDonorDetail(DetailView):
    model = DonationsDemo
    template_name = 'staff/view_donor_detail.html'
    context_object_name = 'donor'


class DonorUpdateView(UpdateView):
    model = DonationsDemo
    fields = ('name',
              'date',
              'amt'
              )
    template_name = 'staff/update_donor_detail.html'
    context_object_name = 'donor'

    def get_success_url(self):
        return reverse('web:view-donor')
