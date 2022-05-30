from django.urls import path

from Facility_Management import views

urlpatterns = [

    path('facility_manager', views.facility_management, name='facility_manager'),
    path('order_facility', views.order_facility, name="order_facility"),
    path('facility_management_order', views.facility_management_client_order, name="facility_management_order"),
    path('facility_logout', views.facility_logout, name="facility_logout"),

]
