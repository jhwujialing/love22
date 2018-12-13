# -*- coding:utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from .views import  xu222ViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.cache import cache_page
urlpatterns = [
    url(r'^input1/$', (cache_page(60*60))(xu222ViewSet.as_view())),
    #url(r'^input1/(?P<pk>[0-9]+)$',xu222ViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)