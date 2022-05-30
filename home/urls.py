from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html',views.home, name='home'),
    path('search', views.search, name='search'),
    path('apply', views.apply, name='apply'),
    path('Show_Available_Jobs.html',views.show_available_jobs,name='ShowAvailableJobs'),
    path('packages.html', views.packages, name='packages'),
    path('about.html', views.about, name='about'),
    path('terms_and_conditions.html', views.terms, name='terms'),
    path('contact.html', views.contact, name='contact'),
    path('submit',views.enquiry1, name='enquiry'),
    path('order',views.onlineorder1, name='online_order'),
    path('activation.html',views.myiactivation, name='activation'),
    path('check', views.finalacti, name='check'),
    path('own_job_request',views.own_job_request, name='own_job_request'),
    path('submit_own_job', views.submit_own_job, name='submit_own_job')




]
