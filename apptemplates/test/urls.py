"""URLs for testing django-apptemplates"""
from django.contrib import admin
from django.conf.urls import url

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
