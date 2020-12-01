from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
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
    BlogUpdateView,
    ViewEventDetail,
    EventUpdateView,
    EventDetail,
    DonorDeleteView,
    EventDeleteView,
    BlogDeleteView,
    FundUpdate,
    InterestedList,
    QueryList,
    QueryDetail,
    RegistrationList,
    RegistryDetail,
    RegistryDeleteView,
    RegistryUpdateView,
)

app_name = "web"
urlpatterns = [
    path('', views.home_page, name='home'),
    path('test/', views.test_page, name='test'),
    path('contact/', views.contact_page, name='contact'),
    path('donor/', views.donor_page, name='donor'),

    path('submission/', views.save_interested_info, name='saveIntDonor'),

    path('contacted/', views.save_query, name='contactQuery'),

    path('registered/', views.save_registry, name='registerParticipation'),

    path('staff/', Login.as_view(), name='staff'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('staff/dashboard/', views.staff_home, name='dashboard'),
    path('about/', views.about, name='about'),
    path('team/', views.team_page, name='team'),
    path('blog/', views.blog_page, name='blog'),
    path('blog/<int:pk>', BlogDetail.as_view(), name='blog-single'),
    path('project/', views.project_page, name='project'),
    path('events/', views.event_page, name='events'),
    path('qr/', views.qr_page, name='qr'),
    path('events/<int:pk>', EventDetail.as_view(), name='event-details'),
    path('garuda/', views.garuda_page, name='garuda'),
    path('phoenix/', views.phoenix_page, name='phoenix'),
    path('swiftSat/', views.swiftSat_page, name='sat'),

    path('account/password_change/', PasswordChange.as_view(), name='change-password'),
    path('account/password_change_complete/', views.password_change_complete, name='change-password-completed'),

    path('view/donors/', login_required(DonorList.as_view(), login_url='/staff'),
         name='view-donor'),
    path('view/donors/<int:pk>', login_required(ViewDonorDetail.as_view(), login_url='/staff'),
         name='donor-detail'),
    path('view/donors/<int:pk>/update/', login_required(DonorUpdateView.as_view(), login_url='/staff'),
         name='update-donor'),
    path('view/donors/<int:pk>/delete/', login_required(DonorDeleteView.as_view(), login_url='/staff'),
         name='delete-donor'),

    path('view/events/', login_required(EventList.as_view(), login_url='/staff'),
         name='view-event'),
    path('view/events/<int:pk>', login_required(ViewEventDetail.as_view(), login_url='/staff'),
         name='event-detail'),
    path('view/events/<int:pk>/update/', login_required(EventUpdateView.as_view(), login_url='/staff'),
         name='update-event'),
    path('view/events/<int:pk>/delete/', login_required(EventDeleteView.as_view(), login_url='/staff'),
         name='delete-event'),

    path('view/blogs/', login_required(BlogList.as_view(), login_url='/staff'),
         name='view-blog'),
    path('view/blogs/<int:pk>', login_required(ViewBlogDetail.as_view(), login_url='/staff'),
         name='blog-detail'),
    path('view/blogs/<int:pk>/update/', login_required(BlogUpdateView.as_view(), login_url='/staff'),
         name='update-blog'),
    path('view/blogs/<int:pk>/delete/', login_required(BlogDeleteView.as_view(), login_url='/staff'),
         name='delete-blog'),

    path('view/interested/', login_required(InterestedList.as_view(), login_url='/staff'),
         name='view-interested'),
    path('view/query/', login_required(QueryList.as_view(), login_url='/staff'),
         name='view-query'),
    path('view/query/<int:pk>', login_required(QueryDetail.as_view(), login_url='/staff'),
         name='query-detail'),

    path('view/registry/', login_required(RegistrationList.as_view(), login_url='/staff'),
         name='view-registration'),
    path('view/registry/<int:pk>', login_required(RegistryDetail.as_view(), login_url='/staff'),
         name='registry-detail'),
    path('view/registry/<int:pk>/update/', login_required(RegistryUpdateView.as_view(), login_url='/staff'),
         name='update-registry'),
    path('view/registry/<int:pk>/delete/', login_required(RegistryDeleteView.as_view(), login_url='/staff'),
         name='delete-registry'),


    path('donor/registration/', views.donor_registration_view, name='donor-registration'),

    path('blog/create/', views.blog_creation_view, name='blog-creation'),

    path('event/create/', views.event_creation_view, name='event-creation'),

    path('fund/<int:pk>', login_required(FundUpdate.as_view(), login_url='/staff'), name="view-fund"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

