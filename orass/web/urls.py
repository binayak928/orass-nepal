from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

from .views import (
    Login
)

app_name = "web"
urlpatterns = [
    path('', views.home_page, name='home'),
    path('test/', views.test_page, name='test'),
    path('contact/', views.contact_page, name='contact'),
    path('donor/', views.donor_page, name='donor'),

    path('staff/', Login.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('staff/dashboard/', views.staff_home, name='dashboard'),
]