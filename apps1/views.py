# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import generics
from .serializers import xu222Serializer
from .models import xu222
# Create your views here.
#@cache_page(60 * 15) # 秒数，这里指缓存 15 分钟，不直接写900是为了提高可读性
class xu222ViewSet(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
	template_name = "index.html"
	serializer_class = xu222Serializer
	#queryset = yyyd.objects.all()
	@method_decorator(cache_page(60*15))
	def get(self, request, format=None):
		return Response('爱兔兔')
	@method_decorator(cache_page(60*15))
	def post(self, request, format=None):
		'''
		name_property = request.data['name_property']
		address_property =request.data['address_property']
		legalperson_property = request.data['legalperson_property']
		ID_property = request.data['ID_property']
		ppxs_input = float(request.data['ppxs_input'])
		pageNo = int(request.data['pageNo'])
		zz = input1(name_property,address_property,legalperson_property,ID_property,ppxs_input,pageNo)
		'''
		return Response('aa')