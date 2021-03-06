"""holandes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
 #extra_patterns = [
#   url(r'^reports/$', credit_views.report),
#  url(r'^reports/(?P<id>[0-9]+)/$', credit_views.report),
#  url(r'^charge/$', credit_views.charge),
#]
"""

from django.conf.urls import url
from core import views as main_views

urlpatterns = [
    url(r'^$', main_views.home),
]