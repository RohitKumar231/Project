"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from app1.cancle_appointment import cancle_appointment
from app1.register_for_profession import register_for_profession
from app1.update_appointment import update_appointment
from app1.views import update_appointment_page, login_signup, home

urlpatterns = [
    path('home/', home),
    path('register_for_profession/',register_for_profession),
    path('cancle_appointment/',cancle_appointment),
    path('update_appointment/',update_appointment),
    path('update_appointment_page/', update_appointment_page),
    path('login_signup/',login_signup),

]
