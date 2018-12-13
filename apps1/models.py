# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class xu222(models.Model):
	#name_property = models.CharField(max_length=600, blank=True, null=True)
	#address_property =models.CharField(max_length=600, blank=True, null=True)

	#legalperson_property = models.CharField(max_length=600, blank=True, null=True)
	#ID_property = models.CharField(max_length=600, blank=True, null=True)
	#ppxs_input = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
	#pageNo = models.IntegerField(blank=True, null=True)
	'''
	class Meta:
		verbose_name = "University"
		verbose_name_plural = "Universities"
	'''

	def __unicode__(self):
		return self.name