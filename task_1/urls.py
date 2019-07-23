"""task_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from flights.views import FlightsList, BookingsList,BookingRetrieve , BookingUpdate , BookingCancel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', FlightsList.as_view(), name="flights-list"),
    path('bookings/', BookingsList.as_view(), name="bookings-list"),
    path('BookingRetrieve/<int:azeeza>/', BookingRetrieve.as_view(), name="booking-details"),
    path('BookingUpdate/<int:ali>/', BookingUpdate.as_view(), name="update-booking"),
    path('BookingCancel/<int:maryme>/', BookingCancel.as_view(), name="cancel-booking")


]
