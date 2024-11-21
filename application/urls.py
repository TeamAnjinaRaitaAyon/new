from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('EntryPage/', views.EntryPage, name='EntryPage'),
    path('RegistrationFormPage/',views.RegistrationFormPage,name='RegistrationFormPage'),
    path('',views.WelcomePage, name='WelcomePage'),
    path('ServicePage/',views.ServicePage, name='ServicePage'),
    path('NewsDetailsPage/',views.NewsDetailsPage, name='NewsDetailsPage'),
    path('HomePage',views.HomePage, name='HomePage'),
    path('VotingPage/',views.VotingPage,name='VotingPage'),
    path('ElectionSetupPage/',views.ElectionSetupPage,name='ElectionSetupPage'),
    path('MinistryPage/',views.MinistryPage,name='MinistryPage'),
    path('MinistySetupPage/',views.MinistrySetupPage,name='MinistrySetupPage'),

    path('EducationPage',views.EducationPage,name='EducationPage'),
    path('EntertainmentPage/',views.EntertainmentPage,name='EntertainmentPage'),
    path('Am_I_A_Citizen/',views.Am_I_A_CitizenPage,name='Am_I_A_CitizenPage'),
    path('NewsDetailsPage/<path:news>/',views.NewsDetailsPage, name='NewsDetailsPage'),
    path('AboutPage/',views.AboutPage,name='AboutPage'),
    path('ContactPage/',views.ContactPage,name='ContactPage'),
    path('HelpPage/',views.HelpPage,name='HelpPage'),
    path('TicketsPage/',views.TicketsPage,name='TicketsPage'),

    path('TransportationMain', views.TransportationMain, name='TransportationMain'),
    

    path('HealthcareMain',views.HealthcareMain,name='HealthcareMain'),
    path('get_hospitals/', views.get_hospitals, name='get_hospitals'),
    path('get_doctors/', views.get_doctors, name='get_doctors'),
    path('get_visiting_hours/', views.get_visiting_hours, name='get_visiting_hours'),
    
    
    path('ThankYou', views.ThankYou, name='ThankYou'),

    path('<path:undefined_path>/', views.Undefine),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
