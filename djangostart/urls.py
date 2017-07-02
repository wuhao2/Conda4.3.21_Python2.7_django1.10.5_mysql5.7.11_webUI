# _*_ coding=utf-8 _*_

"""djangostart URL Configuration

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
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from apps.message.views import getform

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^form/$', getform, name='go_form'),
    url(r'^form_go/$', getform, name='go_form'),
    #coresponding html page {%url 'go_form' %}
    # using his verbor name, you can change form into form_go, but no need to change on html page
    # it also work

]
