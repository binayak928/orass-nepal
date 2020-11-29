from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView
from .forms import DonorRegistrationForm, BlogCreationForm, EventCreationForm
from .models import DonationsDemo, Blog, Event
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
    all_blogs = Blog.objects.all()
    context = {
        "blogs": all_blogs
    }
    return render(request, 'web/blog.html', context)


# def blog_detail(request):
#     all_blogs = Blog.objects.all()
#     context = {
#         "blogs": all_blogs
#     }
#     return render(request, 'web/blog_detail.html', context)


class BlogDetail(DetailView):
    model = Blog
    template_name = 'web/blog_detail.html'
    context_object_name = 'blog'


def project_page(request):
    context = {}
    return render(request, 'web/project.html', context)


def event_page(request):
    all_events = Event.objects.all()
    context = {
        "events": all_events
    }
    return render(request, 'web/event.html', context)


class EventDetail(DetailView):
    model = Event
    template_name = 'web/registration.html'
    context_object_name = 'event'


# def detail_page(request):
#     context = {}
#     return render(request, 'web/registration.html', context)


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
            donation = DonationsDemo(name=data['name'],
                                     date=data['date'],
                                     amt=data['amt'],
                                     )
            donation.save()
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


class EventList(ListView):
    model = Event
    template_name = 'staff/view_event.html'


class ViewEventDetail(DetailView):
    model = Event
    template_name = 'staff/view_event_detail.html'
    context_object_name = 'event'


class EventUpdateView(UpdateView):
    model = Event
    fields = ('date',
              'start',
              'end',
              'title',
              'address_street',
              'address_city',
              'address_country',
              'description',
              'organizer',
              'phone',
              'email',
              'picture'
              )
    template_name = 'staff/update_event_detail.html'
    context_object_name = 'event'

    def get_success_url(self):
        return reverse('web:view-event')


class BlogList(ListView):
    model = Blog
    template_name = 'staff/view_blog.html'
    context_object_name = 'blogs'


class ViewBlogDetail(DetailView):
    model = Blog
    template_name = 'staff/view_blog_detail.html'
    context_object_name = 'blog'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('author',
              'post_date',
              'title',
              'category',
              'body'
              )
    template_name = 'staff/update_blog_detail.html'
    context_object_name = 'blog'

    def get_success_url(self):
        return reverse('web:view-blog')


@login_required(login_url="/staff")
def blog_creation_view(request):
    if request.method == "POST":
        form = BlogCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_blog = Blog(author=data['author'],
                            post_date=data['post_date'],
                            title=data['title'],
                            category=data['category'],
                            body=data['body'],
                            )
            new_blog.save()
            return redirect('web:view-blog')
    else:
        form = BlogCreationForm()
    return render(request, 'staff/blog_creation.html', {'form': form})


@login_required(login_url="/staff")
def event_creation_view(request):
    if request.method == "POST":
        form = EventCreationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            new_event = Event(date=data['date'],
                              start=data['start'],
                              end=data['end'],
                              title=data['title'],
                              address_street=data['address_street'],
                              address_city=data['address_city'],
                              address_country=data['address_country'],
                              description=data['description'],
                              organizer=data['organizer'],
                              phone=data['phone'],
                              email=data['email'],
                              picture=data['picture']
                              )
            new_event.save()
            return redirect('web:view-event')
    else:
        form = EventCreationForm()
    return render(request, 'staff/event_creation.html', {'form': form})
