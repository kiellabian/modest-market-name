from django.conf.urls import include, url
from django.contrib import admin

from name import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
]