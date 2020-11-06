from django.conf.urls import url
from django.urls import path, include
from . import views

# from .views import (
#
# )
app_name = "web"
urlpatterns = [
    path('', views.home_page, name='home'),
    path('test', views.test_page, name='test'),
    path('contact', views.contact_page, name='contact'),
]