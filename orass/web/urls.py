from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

from .views import (
    Login,
    PasswordChange,
    DonorList,
    ViewDonorDetail,
    DonorUpdateView,
    EventList,
    BlogList,
    BlogDetail,
    ViewBlogDetail,
    BlogUpdateView
)

app_name = "web"
urlpatterns = [
    path('', views.home_page, name='home'),
    path('test/', views.test_page, name='test'),
    path('contact/', views.contact_page, name='contact'),
    path('donor/', views.donor_page, name='donor'),

    path('staff/', Login.as_view(), name='staff'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('staff/dashboard/', views.staff_home, name='dashboard'),
    path('faq/', views.faq_page, name='faq'),
    path('about/', views.about, name='about'),
    path('team/', views.team_page, name='team'),
    path('blog/', views.blog_page, name='blog'),
    path('blog/<int:pk>', BlogDetail.as_view(), name='blog-single'),
    path('project/', views.project_page, name='project'),
    path('events/', views.event_page, name='events'),
    path('events/detail/', views.detail_page, name='event-details'),

    path('account/password_change/', PasswordChange.as_view(), name='change-password'),
    path('account/password_change_complete/', views.password_change_complete, name='change-password-completed'),

    path('view/donors/', login_required(DonorList.as_view(), login_url='/staff'),
         name='view-donor'),
    path('view/donors/<int:pk>', login_required(ViewDonorDetail.as_view(), login_url='/staff'),
         name='donor-detail'),
    path('view/donors/<int:pk>/update/', login_required(DonorUpdateView.as_view(), login_url='/staff'),
         name='update-donor'),

    path('view/events/', login_required(EventList.as_view(), login_url='/staff'),
         name='view-event'),

    path('view/blogs/', login_required(BlogList.as_view(), login_url='/staff'),
         name='view-blog'),
    path('view/blogs/<int:pk>', login_required(ViewBlogDetail.as_view(), login_url='/staff'),
         name='blog-detail'),
    path('view/blogs/<int:pk>/update/', login_required(BlogUpdateView.as_view(), login_url='/staff'),
         name='update-blog'),

    path('donor/registration/', views.donor_registration_view, name='donor-registration'),

    path('blog/create/', views.blog_creation_view, name='blog-creation'),
]
